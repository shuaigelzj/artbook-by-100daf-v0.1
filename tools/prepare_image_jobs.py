# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'替换制品登记.json').read_text())
common='Use case: stylized-concept. Roblox survival game replacement asset concept in a coherent simplified LOW-POLY 3D family. Chunky bevels, clearly faceted surfaces, matte materials, 5-8 readable main shapes, restrained wear and restrained technology glow. Neutral warm beige studio background, soft shadows, clean complete isolated object, no environment, no real people, no caption, no labels, no watermark. This is visual game concept art, NOT a functional blueprint. No realistic gore, decay, blood, exposed organs or gun cutaways. Do NOT copy square machine plinths or energy generators from style references. NO base or platform unless intrinsically part of edible bowl; maintain appropriate natural silhouette. '
masters=[];jobs=[]
for key,g in data['groups'].items():
    records=[r for r in data['records'] if r['category']==key]
    # Stable original-slot order; branch/rank is documented rather than false global tier sorting.
    grid='4 columns, 4 rows' if len(records)<=16 else '4 columns, 5 rows'
    p=common+'Create a FAMILY DESIGN MASTER contact sheet, '+grid+', exactly '+str(len(records))+' distinct objects, one object per occupied cell, leave remaining cells blank. All cells use same elevated front-right camera and identical material language. Each object complete, clear separation, generous margins. No three views here; ONE view per object. Keep handgrip/attachment dimensions comparable within families; animals retain squirrel < hyena < bear/deathclaw relative sizes, no forced equal real-world height. Composition cell order is LEFT TO RIGHT, TOP TO BOTTOM. The designs in exact cell order:\n'
    p+='\n'.join(str(i+1)+'. '+r['visual'] for i,r in enumerate(records))
    masters.append(dict(key=key,prompt=p,refs=[str(ROOT/g['style_ref'])],path=g['name']+'/versions/v1/overview_v1.png',status='planned'))
    for i,r in enumerate(records):
        special=''
        if key=='food':special='IMPORTANT: draw the FOOD CUT itself, NOT its source animal. Raw/cooked pairs must keep the corresponding silhouette; no gore. Herbs/soups are stylized game items, no real medicinal claim. '
        if key=='equipment':special='IMPORTANT: wearable SLOT PART ONLY. Chest pieces end above waist, hood/mask is headgear only, boots are paired footwear, scarf is neck drape. Absolutely no full humanoid, no mannequin, no human skin. '
        if key=='ranged':special='IMPORTANT: non-firing inert fictional GAME PROP only, no construction drawing, no internal mechanism or real dimensions. Bows include one separate arrow only as visually specified. '
        p=common+'Create ONE LANDSCAPE model-reference sheet of EXACTLY THREE consistent views of the SAME asset. Views horizontally arranged: '+g['view_prompt']+'. Keep same scale and baseline, complete object in each view, enough margins, no cropping. Natural slender/long object is NOT forced into a square, do not add any machinery plinth or material input port. Reference image is the family design master; select asset cell '+str(i+1)+' (row '+str(i//4+1)+', column '+str(i%4+1)+') ONLY, other cells are STYLE references not extra subjects. Preserve this selected design and simplify clutter. '+special+'Subject visual: '+r['visual']+' Preserve all essential head/leg/limb/barrel/armhole counts in each view; hidden parts correctly occlude, never invent more parts. '
        jobs.append(dict(id=r['id'],key=key,name=r['target'],prompt=p,refs=[str(ROOT/g['name']/'versions/v1/overview_v1.png')],path=r['images']['v1'],status='planned'))
(ROOT/'制作任务.json').write_text(json.dumps({'masters':masters,'items':jobs},ensure_ascii=False,indent=2))
for key,g in data['groups'].items():
    rs=[j for j in jobs if j['key']==key]
    master=next(m for m in masters if m['key']==key)
    text='# '+g['name']+'｜v1生成提示词\n\n生成方式：内置 imagegen。图像参考仅用于视觉设计，非原游戏3D模型。\n\n## 母图\n\n'+master['prompt']+'\n\n'
    text+='\n'.join('## '+j['id']+' '+j['name']+'\n\n'+j['prompt']+'\n\n' for j in rs)
    (ROOT/g['name']/'prompts.md').write_text(text)
print('Prepared',len(masters),'family masters and',len(jobs),'individual sheets')
