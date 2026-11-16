# -*- coding: utf-8 -*-
from pathlib import Path
import sys, json, shutil, fcntl
root = Path(__file__).resolve().parent.parent
key, source, target = sys.argv[1:4]
dst = root / target
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, str(dst))
with (root / '.image-jobs.lock').open('w') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    path = root / '制作任务.json'
    data = json.loads(path.read_text(encoding='utf8'))
    for job in data['masters'] + data['items']:
        if job.get('id', job.get('key')) == key:
            job.update(status='generated', source_image=source)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf8')
print(key + ' saved')
