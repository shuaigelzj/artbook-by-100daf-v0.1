from pathlib import Path
import json, shutil
from PIL import Image

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent
OUT = ROOT / 'dist'
(OUT / 'assets').mkdir(parents=True, exist_ok=True)
(OUT / 'documents').mkdir(exist_ok=True)

SOURCE_PROJECTS = json.loads((ROOT / 'catalog.json').read_text(encoding='utf8'))['projects']

def asset(project_id, name):
    src = SOURCE / name
    if not src.exists(): raise FileNotFoundError(str(src))
    dest = project_id + '-' + src.stem + '.webp'
    if (OUT / 'assets' / dest).exists() and (OUT / 'assets' / dest).stat().st_mtime >= src.stat().st_mtime:
        return 'assets/' + dest
    with Image.open(src) as im:
        im.convert('RGB').save(OUT / 'assets' / dest, 'WEBP', quality=88, method=6)
    return 'assets/' + dest

data = []
for n, project in enumerate(SOURCE_PROJECTS, 1):
    record = dict(project)
    record.update(number=str(n).zfill(2), count=len(project['items']), iterations=len(project['versions']))
    record['overview'] = asset(project['id'], project['overview'])
    record['items'] = []
    for item in project['items']:
        row = dict(item)
        row.pop('inherited', None)
        row['images'] = {v: asset(project['id'], path) for v, path in item['images'].items()}
        record['items'].append(row)
    record['fixes'] = [dict(f, before=asset(project['id'], f['before']), after=asset(project['id'], f['after'])) for f in project.get('fixes', [])]
    record['documents'] = []
    for index, document in enumerate(project['documents']):
        name = project['id'] + '-' + str(index+1) + '-' + Path(document['path']).name
        shutil.copyfile(SOURCE / document['path'], OUT / 'documents' / name)
        record['documents'].append(dict(name=document['name'], url='documents/' + name))
    archive = SOURCE / project['folder'] / (project['folder'] + '-v1-图片集.zip')
    if archive.exists():
        shutil.copyfile(archive, OUT / 'documents' / (project['id'] + '-originals.zip'))
        record['documents'].append(dict(name='原始 PNG 图片集与输入文档', url='documents/' + project['id'] + '-originals.zip'))
    data.append(record)
    shutil.copyfile(OUT / 'index.html', OUT / (project['id'] + '.html'))
(OUT / 'data.js').write_text('window.DELIVERABLES = ' + json.dumps(data, ensure_ascii=False) + ';', encoding='utf8')
print('Built', len(data)+1, 'pages;', len(list((OUT / 'assets').iterdir())), 'images')
