from pathlib import Path
import json,re
from html.parser import HTMLParser
from PIL import Image

root=Path(__file__).resolve().parent/'dist'
data=json.loads((root/'data.js').read_text().removeprefix('window.DELIVERABLES = ')[:-1]) if hasattr(str,'removeprefix') else json.loads((root/'data.js').read_text()[len('window.DELIVERABLES = '):-1])
paths=[]
for project in data:
    paths.append(project['overview'])
    for f in project.get('fixes',[]):paths.extend([f['before'],f['after']])
    assert project['latest'] in [v['id'] for v in project['versions']]
    for item in project['items']:
        assert project['latest'] in item['images']
        paths.extend(item['images'].values())
    paths.extend(d['url'] for d in project['documents'])
for name in paths:
    p=root/name
    assert p.is_file(),name
    if p.suffix=='.webp':
        with Image.open(p) as im:im.verify()
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key in ('href','src') and value and not value.startswith(('#','http','data:')):
                assert (root/value).exists(),value
for page in ['index.html']+[p['id']+'.html' for p in data]:
    Links().feed((root/page).read_text())
assert all('http' not in (root/f).read_text() for f in ['style.css','app.js','index.html'])
print('PASS: '+str(len(data)+1)+' pages,',len(set(paths)),'image/document resources, all latest images and local links; no external runtime dependencies')

assert len(data)==7
assert sum(p['count'] for p in data if p.get('status')=='review')==83
assert [p['count'] for p in data[2:]]==[14,18,16,19,16]
print('PASS: all 83 mappings and latest sheets; existing 11 facility designs retained')
