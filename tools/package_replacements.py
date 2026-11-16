# -*- coding: utf-8 -*-
from pathlib import Path
import json, hashlib, zipfile
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'替换制品登记.json').read_text(encoding='utf8'))
jobs=json.loads((ROOT/'制作任务.json').read_text(encoding='utf8'))
assert len(meta['records'])==83
assert len({r['id'] for r in meta['records']})==83
files=[]
for key,g in meta['groups'].items():
 rows=[r for r in meta['records'] if r['category']==key]
 master=next(j for j in jobs['masters'] if j['key']==key)
 paths=[master['path']]+[r['images']['v1'] for r in rows]
 for path in paths:
  p=ROOT/path
  assert p.exists(),path
  with Image.open(p) as im:
   im.verify()
  files.append(dict(path=path,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 lines=['# '+g['name']+'｜制作记录 v1','','状态：首轮概念图片集，等待同事评审；尚无反馈修订版。','',
 '## 制作链路','','1. 对照原工程素材清单与明细逐条配对；保留原槽位、用途、设定出处及改编决定。',
 '2. 按《制品输入模板》固定本组规则与逐件输入，见 `input/描述表.md`。',
 '3. 参考能源 v7、机床 v2 与 sample 的简化语言，生成组内风格母图。',
 '4. 每件引用母图中的指定格子，独立生成一张三视图；不使用裁切母图代替三视图。',
 '5. 核对文件、编号、PNG 解码及网站资源覆盖；原始生成图保留，网站另转 WebP。','',
 '## 统一与检查要点','','- 视角：'+g['views']+'。','- 比例：'+g['scale']+'。',
 '- 分支序位表达原用途/能力，调试项序位0不进入正常成长；不同支线不强行比较数值。',
 '- 图片不含名称，身份以稳定编号和页面配对表对应。母图按原素材槽位从左到右、从上到下排列。',
 '- 同组材质、背景与主要形体已统一；三视图用于轮廓沟通。隐蔽面的几何、握点、穿戴接口和骨架仍需建模时结合输入表确定，图片不是带尺寸工程图。','',
 '## 本轮文件','','| 编号 | 原素材 → 制品 | 输入/图像 |','| --- | --- | --- |']
 for r in rows:
  lines.append('| '+r['id']+' | '+r['original']+' → '+r['target']+' | [三视图](final/'+Path(r['images']['v1']).name+') |')
 lines+=['','## 下一轮评审入口','','请按编号反馈：保留/替换的配对、轮廓辨识、同支线递进、三视图结构、玩法改编是否采用。评审通过后再增加真实 v2；本轮不把母图和单件图伪记成两个迭代版本。','']
 if key=='melee':
  lines += ['## 制作内修正', '', 'MEL-016 初稿与 MEL-017 过于相似，已重绘为长导板、深色动力护壳、双握位的战斗型。母图保留前置探索状态，单件图为当前造型。详见 `修正记录.md`。', '']
 (ROOT/g['name']/'iterations.md').write_text('\n'.join(lines),encoding='utf8')
 docs=['input/描述表.md','brief.md','prompts.md','iterations.md']
 if key=='melee':docs+=['修正记录.md','versions/v1/exploration/MEL-016_initial.png']
 archive=ROOT/g['name']/(g['name']+'-v1-图片集.zip')
 with zipfile.ZipFile(str(archive),'w',zipfile.ZIP_DEFLATED) as z:
  for rel in paths:
   z.write(str(ROOT/rel),rel)
  for rel in docs:
   z.write(str(ROOT/g['name']/rel),g['name']+'/'+rel)
print('Verified 83 individual PNG sheets + 5 family masters; wrote 5 group packages')
(ROOT/'图片交付清单.json').write_text(json.dumps({'items':83,'masters':5,'files':files},ensure_ascii=False,indent=2),encoding='utf8')
with zipfile.ZipFile(str(ROOT/'废土素材替换-v1-完整图片与文档.zip'),'w',zipfile.ZIP_DEFLATED) as z:
 for row in files:z.write(str(ROOT/row['path']),row['path'])
 for g in meta['groups'].values():
  if g['name']=='近战武器':
   for rel in ['修正记录.md','versions/v1/exploration/MEL-016_initial.png']:z.write(str(ROOT/g['name']/rel),g['name']+'/'+rel)
  for rel in ['input/描述表.md','brief.md','prompts.md','iterations.md']:
   z.write(str(ROOT/g['name']/rel),g['name']+'/'+rel)
 for rel in ['替换对应关系表.md','替换对应关系表.csv','替换制品登记.json','制作任务.json','图片交付清单.json','制品输入模板.md','制品制作流程.md']:
  z.write(str(ROOT/rel),rel)
