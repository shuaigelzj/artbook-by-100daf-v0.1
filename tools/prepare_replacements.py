from pathlib import Path
import json,re,csv

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL=Path('/Users/lzj/vibegame/100daf-rb/modeling-assets')
def clean(s): return re.sub(r'\*\*|`','',s).strip()
def rows(text,section):
    match=re.search(r'^## '+str(section)+r'\.[\s\S]*?(?=^## |\Z)',text,re.M)
    return [[clean(c) for c in line.strip().strip('|').split('|')] for line in match.group().splitlines() if line.startswith('| ') and not re.match(r'\|\s*[-:]',line)][1:]
inventory=(ORIGINAL/'建模素材清单.md').read_text()
details=(ORIGINAL/'建模素材明细表.md').read_text()
catalog_files={'C':'cold_and_powered_weapons_catalog.md','G':'firearms_and_weapons_catalog.md','E':'personal_equipment_catalog_two_tables.md','F':'wasteland_food_and_ingredients.md','A':'wasteland_creatures_catalog.md'}
catalogs={}
for code,filename in catalog_files.items():
    result={}
    for line in (ROOT/'tmp'/filename).read_text().splitlines():
        if not line.startswith('|'): continue
        cells=[clean(c) for c in line.strip().strip('|').split('|')]
        if cells[0].isdigit(): result[int(cells[0])]=cells
    catalogs[code]=result

# Indexes refer to actual rows in the original inventory, not invented gameplay ranks.
# category, original row, source refs, target, branch, display rank, adaptation, visual specification
R=[]
def add(cat,index,refs,target,branch,rank,adapt,visual):
    R.append(dict(category=cat,index=index,refs=refs,target=target,branch=branch,rank=rank,adaptation=adapt,visual=visual))

add('animals',0,'A7','幼年变异鬣狗','荒野主线',1,'幼体改编；保留早期可驯服生态位','One juvenile SINGLE-headed hyena, oversized ears, short dark mane, ochre faceted coat with dark spots, thin limbs, alert expression; no wounds.')
add('animals',1,'A7','双头变异鬣狗','荒野主线',2,'选用设定中的双头变体；需双头骨架','Adult hyena with EXACTLY TWO adjacent heads on one torso, dark bristled mane, ochre patchy coat, muscular front shoulders, one tail; no gore.')
add('animals',2,'A2','妖怪·林地型','荒野主线',3,'变异熊轮廓；腐烂改为无血腥硬皮斑块','Hunched mutant bear, dark brown sparse blocky fur, pale grey tough skin patches, broad shoulders, blunt tusk-like canines and large paws; no decay or wounds.')
add('animals',3,'A3','铁背猿','荒野主线',4,'以智慧异种替代高速猫科；需新攀行/近战骨架','Powerful black-furred gorilla, long arms, squat legs, layered BLACK armored scales over upper back, strong hands, low aggressive stance; no held weapon.')
add('animals',4,'A1','死亡之爪','荒野主线',5,'压缩原著巨型体量为后期精英兽；不声称沿用熊骨架','Upright digitigrade black-scaled reptilian predator, long heavy tail, two muscular arms ending in THREE oversized curved claws each, angular horned head, amber eyes; no blood.')
add('animals',5,'A8','变异野猪','湿地主线',1,'保持野猪冲撞与召唤小怪复用','Stocky dark brown wild boar, thick charcoal needle-like mane, one pair long upward ivory tusks, broad flat snout, short robust legs.')
add('animals',6,'A13','裂爪蟹','湿地主线',2,'蟹替鳄鱼；需八足/双钳骨架和碰撞适配','Low broad mutant crab, domed grey mineral shell with a few moss patches, EXACTLY TWO giant forward pincers and EIGHT walking legs, small eyes, no extra claws.')
add('animals',7,'A31','黑鸟·地栖型','湿地采猎',1,'将巨大黑鸟改为落地采猎禽；是否飞行另配','Chunky standing mutant raven, glossy matte charcoal faceted feathers, folded wings, thick curved black beak, stout legs, broad claws, subtle copper edge feathers; no flight pose.')
add('animals',8,'A11','变异雪狼','雪原主线',2,'雪地分支；非全物种科技升级','White and grey thick-furred wolf, compact ears, broad paws, icy blue eyes, bushy tail, angular fur tufts, no glowing magic.')
add('animals',9,'A2','妖怪·雪原型','雪原主线',3,'同源雪熊改型；毛色与保暖结构适配','Hunched snow mutant bear, cream-white chunky fur and blue-grey tough skin plates, broad hump, dark muzzle, large paws, visible blunt canine teeth; no wounds.')
add('animals',10,'A35','变异松鼠','温顺采猎',1,'保留兔子的受击逃跑角色；兔脚掉落需改名','Small russet mutant squirrel, giant fluffy curled tail, large dark eyes, tiny paws, rounded ears and cream belly, benign alert stance.')
add('animals',11,'A5','双头牛','温顺采猎',3,'温顺驮兽；双头与原水牛骨架不同','Gentle stocky bovine with EXACTLY TWO adjacent horned heads and TWO low fat humps, dusty brown hide, four strong legs, one tail; no saddles.')
add('animals',12,'A6','大角鹿','温顺采猎',2,'原仅预制体；预备资产不接入主线','Tall brown deer with pale flank spots, long slim legs, large symmetric branching antlers, cream muzzle, neutral stance; no saddle.')
add('animals',13,'A12','穴居兽·霜灰型','雪原预备',4,'原仅预制体；穴居兽霜灰配色为适应性改编','Pale slate-grey hairless cave ambush beast, low feline-like quadruped body, long foreclaws, small pale eyes, tapered ears and thick balancing tail, no wounds; not a leopard skin.')

add('melee',0,'C1','热熔破拆斧·测试型','调试预留',0,'管理员伤害9999不进入成长序列；仅测试涂装','Compact tactical breaching axe, dark alloy rectangular head, narrow RED thermal cutting edge, white diagnostic grip band; no lettering.')
add('melee',1,'C15','废旧木柄伐木斧','采集斧系',1,'将双手伐木斧压缩为新手握持尺度','Simple worn single-bit iron axe, chipped compact head, curved brown wooden handle bound with coarse rope, no glow.')
add('melee',2,'C12','81号厂战术短斧','采集斧系',2,'保留伐木3的进阶角色','Clean forged tactical hatchet, broader grey steel blade and squared hammer poll, straight olive wrapped handle, practical steel collar.')
add('melee',3,'C9','战术通用匕首','刀剑系',1,'近身快速副武器','Short thick matte charcoal survival knife, straight single cutting edge, minimal spine serrations, black rubber grip and small guard; one knife only.')
add('melee',4,'C10','军团指挥官军刀','刀剑系',2,'长刀替直剑；需挥砍外形适配','Slightly curved silver military sabre, plain half-basket guard, dark leather grip, restrained bronze pommel; no scabbard.')
add('melee',5,'C3','窒息者氮气动力锤','动力重击',4,'用高压氮气与冷聚变表示原充能重击；不继承雷电神话','Two-handed grey power hammer with CYLINDRICAL chamber head, short front impact cone, small blue power cartridge on shaft and one pressure collar, chunky black grip.')
add('melee',6,'C13','矛尖长柄战斧','采集斧系',3,'保留强化采集与长柄两用定位','Long steel-handled axe with wide forged chopping blade and one straight TOP spear spike, dark rubber two-handed grip, heavy reinforced collar.')
add('melee',7,'C9,C1','高频能量护刃直刀','刀剑系',4,'实刃加能源护刃为改编；格挡与耗能机制需对接','Long solid titanium straight blade with a THIN cyan energized edge, compact battery guard, dark rubber grip; blade is solid metal, not pure light beam.')
add('melee',8,'C12','精锻合金短斧','采集斧系',2.5,'宝石表现改为精锻合金与状态条；低于长柄采集档','Precision forged silver-grey hatchet, faceted wedge blade, dark reinforced grip, small non-glowing cyan inspection inset, no crystal blade.')
add('melee',9,'C23','合金钢筋投枪','长柄刺击',2,'将宝石矛改为精加工金属尖；本项仍为近战外观','Long rebar-inspired steel spear, polished four-sided spear point, reinforced joint and dark textile mid-grip, no gemstones.')
add('melee',10,'C24,A17','银嘴蛇毒猎矛','长柄刺击',3,'设定长矛与蛇毒组合改编；保留中毒角色','Wooden hunting spear with dark metal triangular barbed point, small SEALED green toxin ampoule below tip, leather wrappings, no dripping fluid.')
add('melee',11,'C9','消光潜行战术刀','刀剑系',2,'同伤害35的隐蔽侧支，不假装高于军刀','Long slim matte black tactical knife with subtle recurve edge, compact black guard and dark textured grip, minimal violet metal tint, no magic motifs.')
add('melee',12,'E46,E35','低温伺服拳套','控制侧支',3,'机械义肢/手套的低温模块改型；冻结为玩法效果待实现','Pair of wearable dark titanium mechanical gauntlets, broad knuckle plates, ONE small cyan coolant cartridge on each forearm cuff, frost-white edge accents; no arms or mannequin.')
add('melee',13,'C10','军官军刀·冬季礼装','活动侧支',2,'圣诞35伤害保持同档；仅冬季涂装','Military sabre with same practical half-basket geometry, white metal blade, burgundy leather grip and simple cream cloth tie, no candy-cane or fantasy ornaments.')
add('melee',14,'C24,C3','氮气动力破甲长枪','长柄刺击',5,'长矛和氮气锤技术组合改编；不是原文独立命名武器','Advanced long dark alloy spear, heavy narrow four-sided penetrator tip, cylindrical pressure chamber below tip, small blue energy cell, long black grip; no runes.')
add('melee',15,'C5','重型高频链锯刃','动力重击',5,'链锯替大剑；需要握持/命中动画适配','Two-handed heavy chain blade, broad grey guide bar with TWO rows of large blunt stylized carbide teeth, dark compact motor guard, robust handle; no blood.')
add('melee',16,'C6','工业伐木链锯','采集斧系',4,'高效连续采集对应砍树40；换为链锯握持','Compact yellow industrial chainsaw, thick dark toothed guide bar, top loop handle and rear trigger grip, simple side vents, one machine no loose parts.')
add('melee',17,'C1','热熔裁切长刃','刀剑系',5,'热熔斧技术长刃改型；圣光作用需在玩法中重解释','White-grey tactical long cleaver, solid dark blade with thin warm red-white thermal edge, integrated blocky power guard, subtle amber status bar; no religious symbols.')

add('ranged',0,'G6','警用电击枪·测试型','调试预留',0,'9999弹匣仅调试；不作为威力排名','Compact chunky yellow/black stun sidearm, two square emitter apertures, small diagnostic panel, no real-world branding.')
add('ranged',1,'G5','传统转轮手枪','手枪主线',1,'保持基础6发副武器','Simple blued steel six-chamber revolver, modest straight barrel, brown wood grip, plain iron sights; no bullets or labels.')
add('ranged',2,'G16','栓动铁管步枪','长枪主线',1,'保留早期慢射步枪定位','Crude grey pipe bolt-action rifle, one bent bolt handle, rough wooden stock, dark cloth reinforcement, no cross-section or machining details.')
add('ranged',3,'G27','双管猎枪','近距爆发',2,'保留两发霰弹结构','Break-action SIDE-BY-SIDE double barrel hunting shotgun, TWO wide barrels, dark steel receiver, chunky brown wood fore-end and stock.')
add('ranged',4,'G31','高斯精确狙击步枪','长枪预备',5,'原无预制体与明确参数；只预备美术不推断伤害','White/graphite electromagnetic sniper rifle, two long parallel accelerator rails, ONE optic and compact capacitor block, cyan seams, no ammo schematic.')
add('ranged',5,'C20,A17','蛇毒木猎弓','弓系',1,'猎弓加封装毒箭为组合改编','Simple laminated wood hunting bow with leather centre grip, taut string, one separate matching arrow with SEALED green toxin head; keep arrow aside, no firing pose.')
add('ranged',6,'A3','废土燃烧投掷瓶','投掷系',1,'铁背猿条目提及燃烧瓶；瓶体具体外观为游戏化补全','One closed green glass game-prop bottle, wrapped brown cloth neck and orange pictogram band, NO flame, no exposed igniter, no construction diagram.')
add('ranged',7,'G28','联合收割机轻机枪','持续火力',4,'以弹鼓轻机枪代替加特林；射速/弹药动画需适配','Chunky dark steel light machine gun, long ribbed barrel, round drum magazine, folded compact bipod and brown reinforced stock, no tripod or loose cartridges.')
add('ranged',8,'G34','地精肩托火箭筒','范围重火力',3,'炸弹改为肩托火箭筒；须新增肩扛动画和飞行爆炸投射物','Stylized shoulder launcher with dark tube, olive insulated middle, broad stylized inert nose cone, small side sight and rear flared exhaust, no cutaway or ammunition dimensions.')
add('ranged',9,'G4','银蛇精密左轮','手枪主线',2,'精装副武器对应伤害80；弹巢规格按游戏配置适配','Refined silver revolver, black grip, short upper tactical sight rail, subtle snake-scale grip pattern, compact muzzle, no engraving text.')
add('ranged',10,'C2','破晓机械复合弓·低温箭型','弓系',3,'电驱弓原文；低温箭头为控制玩法改编','Graphite/titanium compound bow, exactly two end cams and compact battery grip, small sight, ONE separate arrow with cyan cold-tech collar; no crystal ice bow.')
add('ranged',11,'G24','Pu-9紧凑冲锋枪','自动手枪侧支',3,'替换四管手枪；连发方式和握持须适配','Compact angular charcoal submachine gun, short barrel, straight box magazine and folded wire stock, simple iron sights, no four-barrel assembly.')
add('ranged',12,'G35','旋风转轮榴弹发射器','范围重火力',4,'可复用燃烧瓶改为可补给多发发射器；非自动继承原逻辑','Portable short-barrel grenade launcher, oversized six-lobed cylinder, vertical foregrip and folded skeleton shoulder stock, dark grey/olive with orange hazard inset, no loose grenades.')
add('ranged',13,'G12','黑天鹅G9无托步枪','自动火力',4,'原蒸汽左轮升级为企业步枪；动画/射击频率需调整','Sleek compact black/grey BULLPUP rifle, magazine clearly BEHIND grip, integrated small optic, clean composite angular panels, no glowing energy barrel.')
add('ranged',14,'G30','15式刺针高斯步枪','长枪主线',5,'终极工坊产物以电磁技术表达；三部件拆装需新模块','White/graphite gauss rifle, distinctive TWO parallel tuning-fork accelerator rails, small cyan seams, detachable battery-shaped block and integral optic, clear separate stock/receiver/barrel masses.')
add('ranged',15,'E41','火炬心灵干涉投掷罐','特殊控制',4,'银白扣件放大为投掷罐的组合改型；幽灵改题材效果需开发','Palm-sized silver cylindrical pulse capsule with round blue crystal inset, compact ribbed collar, no cross/religious symbol, closed shell, no cutaway or explosive assembly.')

add('food',0,'F1','羊角薯','基础采集',1,'替代胡萝卜；同为低阶块根','One curved ram-horn-shaped grey-brown tuber, knobby matte skin and two small sprouts; whole plant root only, no plate.')
add('food',1,'F18','鬣狗生肉块','普通肉生熟链',1,'食材图画切块而非原文属主动物','One chunky raw dusky pink meat cut with a small cream fat seam, stylized clean food prop, no blood, no animal body, no plate.')
add('food',2,'F10,F52','菌菇薯泥炖汤','汤品支线',3,'设定食材组合成汤为菜谱改编；饱食100保留为原参数','One simple dented grey metal bowl of beige stew with TWO mushroom chunks and cubed tuber, minimal steam, no spoon or table.')
add('food',3,'F17','双头牛生牛排','牛排生熟链',1,'来源双头牛，图为切片不是双头动物','One thick red-pink faceted raw steak with broad cream fat border, simple marbling, no blood, no whole animal, no plate.')
add('food',4,'F18,F46','炭烤鬣狗肉','普通肉生熟链',2,'217→224沿用肉块轮廓与脂肪位置','One cooked dark brown meat cut, same chunky silhouette and cream fat seam as raw hyena meat, TWO grill marks, no raw flesh, no plate.')
add('food',5,'F17,F35','黄油烤双头牛牛排','牛排生熟链',2,'221→225保留牛排截面形状','One brown grilled steak with thick golden fat rim, TWO diagonal grill marks and ONE tiny butter cube on top, no plate.')
add('food',6,'F14,F28','松子鲜鱼汤','汤品支线',4,'优质汤配方，资料中有明确菜名','One white ceramic bowl of clear golden fish soup, two small fish chunks and THREE pine nuts, tiny herb sprig, no whole fish or cutlery.')
add('food',7,'F3','变异玉米棒','高能作物',2,'替代南瓜；饱食100沿用原游戏不归因真实营养','One thick yellow-brown corn cob with broad stylized kernels and TWO green husk leaves peeled back, matte faceted game prop.')
add('food',8,'F15','变异椰果','高能作物',2,'替代西瓜；补水与食用定位','One round brown fibrous coconut with flat cream exposed top showing white flesh and pale clear centre, small green leaf fragment; no straw.')
add('food',9,'F10','野生松茸','菌菇采集链',1,'安全可食用菇替红菇；配色不代表真实食用判断','One edible stylized mushroom, broad tan-brown cap, thick ivory stem and dark simple gills, no soil clump or pot.')
add('food',10,'F12','精神叶清凉包','特殊补给',2,'精神叶只记提神镇静；解毒效果为游戏化改编而非原文事实','Small bundle of THREE dark green serrated leaves tied with cream twine, one pale BLUE circular status tag without text, no pills or real drug branding.')
add('food',11,'F9','蓝伞菇','有毒资源',1,'蓝色天使在设定中有毒；明确不与原解毒蓝菇混淆','One deep BLUE glowing mushroom with broad cap, pale thin stem, subtle dark cap spots, no green fog, no cartoon smiling face.')
add('food',12,'F10','炭烤松茸串','菌菇采集链',2,'234→237视觉生熟；其他菇转换须单独审查','THREE toasted brown mushroom caps on ONE short wooden skewer, browned edges and cream stems, clean food prop, no plate.')
add('food',13,'F27','裂爪蟹肉浓汤','汤品支线',4,'番茄汤改为高级水产汤，配方为改编','One simple white ceramic bowl of creamy pale orange crab soup with THREE white crab chunks and tiny orange roe garnish, no crab body, no utensils.')
add('food',14,'F24','黑鸟鲜禽肉','禽肉生熟链',1,'239→240用鸟肉截块；不复刻乌鸦整只外观','One clean pink poultry breast-and-leg cut with one small cream bone end, stylized low-poly food prop, no feathers, no blood, no whole bird.')
add('food',15,'F24','柴火烤黑鸟肉','禽肉生熟链',2,'保持239→240同轮廓','One golden-brown cooked poultry breast-and-leg cut with same small cream bone end as raw, two subtle char marks, no plate.')
add('food',16,'F23','妖怪上等生肉','高热肉生熟链',1,'242→243以大块高热异种肉代替重复火鸡','One thick dark rose rectangular prime meat slab with TWO broad cream fat stripes, larger cut than basic meat but same inventory scale, no blood or monster body.')
add('food',17,'F23,F46','蜜烤妖怪肉','高热肉生熟链',3,'高饱食120由精制烹饪表达，不冒充真科技升级','One thick amber-brown glazed prime roast slab, TWO golden fat stripes and three shallow score cuts, no blood, no plate or side dishes.')
add('food',18,'F5','烘暖卡姆果','特殊补给',1,'暖果改编；保暖来自加工状态，不声称原果自发热','One yellow-green oval hard fruit with warm golden toasted patches, short brown stalk and ONE small green leaf, no flames or magical steam.')

add('equipment',0,'E3','龙骑兵助推靴·测试型','调试预留',0,'管理员护甲50仅调试；只画靴子不画全装甲','A matched PAIR of dark grey armored high boots with small inset sole thruster ports and compact ankle plates, no legs, no flames, no standalone platform.')
add('equipment',1,'E21','变异兽皮护胸','护胸主线',1,'原护甲2；保留胸部可穿戴边界','Standalone brown leather CHEST VEST with two shoulder straps, thick hand-stitched panels and FOUR copper rivets, open arm holes, no head/limbs/mannequin.')
add('equipment',2,'E20','军团合金胸甲','护胸主线',2,'原护甲5；板片式防护','Standalone charcoal steel CHEST ARMOR with broad rectangular front plate, two shoulder tabs and dark leather side straps, subtle stamped geometric bird mark, no mannequin or limbs.')
add('equipment',3,'E1','T-10陶钢动力护胸','护胸主线',5,'原护甲8；从全套动力甲提取胸背组件，不增加完整四肢','Standalone compact cobalt-blue powered CHEST AND BACK armor assembly, broad angled ceramic plates, white-grey shoulder tabs, two rear short vents, small central power indicator, open neck/armholes, no helmet or limbs.')
add('equipment',4,'E9','黄金特装护胸·预备型','占位预留',0,'原护甲999占位不进入正式强度序列','Standalone gold-coated heavy chest armor with plain graphite inner carrier, broad beveled plates and simple eagle medallion, no ornate filigree, no limbs or mannequin.')
add('equipment',5,'E18','高分子陶钢防弹胸甲','护胸主线',4,'原护甲7；高于几丁质6，低于动力护胸8','Standalone grey-white faceted ceramic ballistic CHEST carrier with dark fabric straps and one small cyan status inset, angular shoulder tabs, no crystal or fantasy gem, no limbs.')
add('equipment',6,'E34','战术防尘风镜面罩','面部防护',1,'原护甲4；风镜加下半脸布罩的游戏化组合','Wearable standalone amber single-piece dust goggles attached to a dark cloth lower-face mask, simple rear elastic strap, open forehead, no human head.')
add('equipment',7,'E33','双滤罐防毒面具','面部防护',2,'原护甲8；双滤罐取代鸟嘴造型','Standalone black rubber full-face respirator, TWO round glass eye lenses, TWO identical side filter canisters and rear straps, no head or helmet.')
add('equipment',8,'E36','防刺战术军靴','足部防护',1,'原护甲3；保留成对靴件','A matching PAIR of black high tactical boots, chunky ribbed soles, broad toe caps, three simple lace bands and ankle straps, no legs.')
add('equipment',9,'E22','裂爪蟹几丁质护胸','护胸主线',3,'原护甲6；甲壳取代鳄鱼鳞片','Standalone grey-green chitin chest armor, THREE broad overlapping curved shell plates, simple brown shoulder straps, mineral shell texture and two blunt ridges, no limbs.')
add('equipment',10,'E26','密封防辐射头罩','面部防护',2,'原护甲8；提取头罩替羊头面罩，非整套连体服','Standalone pale yellow sealed protective HOOD, wide dark transparent face window, TWO small filter ports and thick black neck seal, no head, torso or gloves.')
add('equipment',11,'E13','重骑兵外骨骼护胸','护胸主线',4.5,'原护甲8同档侧支；仅胸背伺服结构，不画整副机架','Standalone black CHEST armor with two thick shoulder support arches, compact side servo hinges and graphite front ballistic plate, small blue battery at back, no arms/legs.')
add('equipment',12,'E29','粗布遮风围领','颈部防护',1,'斗篷裁成颈部围领；保留减伤0.2角色','Standalone folded sand-brown hoodless neck scarf/cowl, coarse triangular cloth drape, one simple knot and frayed lower edge, no head or full cape.')
add('equipment',13,'E28','魔鬼丝防弹围领','颈部防护',2,'防弹斗篷改成围领；对应减伤0.37','Standalone charcoal silk tactical neck cowl, layered smooth folded collar, short triangular chest drape and ONE silver clasp, subtle woven sheen, no full cape or body.')
add('equipment',14,'E4','海狮密封护胸','环境护胸侧支',5,'原护甲8同档环境分支；只提取胸背水密组件','Standalone teal/navy sealed chest armor, rounded pressure plate, thick dark gasket seams, one compact sonar status inset and two small rear ports, open armholes, no helmet/limbs.')
add('equipment',15,'E16,E31','先锋冬季战术护胸','活动护胸侧支',4,'原护甲7；冬季皮草为适配改编，不假装高于T-10','Standalone sand-grey composite chest vest with neat cream fur collar and dark inset shoulder webbing, compact rear battery panel, no seasonal ornaments, no mannequin/limbs.')

GROUPS={
 'animals':dict(name='动物',section=4,detail_section=3,prefix='ANI',english='WASTELAND FAUNA',views='正面 / 右侧 / 背面',view_prompt='front elevation, RIGHT SIDE profile with nose pointing RIGHT, rear elevation; neutral grounded stance with identical anatomy',scale='按生态位保留小型/中型/大型相对比例；不同物种不强制等大，无设施底座',style_ref='sample/BIO-0016_model.png'),
 'melee':dict(name='近战武器',section=9,detail_section=8,prefix='MEL',english='MELEE EQUIPMENT',views='正视 / 右侧 / 背视',view_prompt='broadside face view showing blade profile, narrow edge-on SIDE view, opposite broadside face view; long axis vertical; for gauntlets matched pair in each view',scale='统一Roblox握把粗细；短刀/斧/长矛分长度族，不将匕首拉成大剑；无底座',style_ref='机床/machining_same_scale_overview_v2.png'),
 'ranged':dict(name='远程与投掷武器',section=10,detail_section=9,prefix='RNG',english='RANGED & THROWABLES',views='左侧 / 俯视 / 右侧',view_prompt='LEFT broadside profile, TOP DOWN plan, RIGHT broadside profile; gun barrel points LEFT in left profile and RIGHT in right profile; complete static game prop, no firing',scale='统一握持比例；短枪/长枪/弓/投掷物分长度族，无底座；不添加设施投料口',style_ref='机床/machining_same_scale_overview_v2.png'),
 'food':dict(name='食物',section=13,detail_section=12,prefix='FOD',english='FOOD & INGREDIENTS',views='斜前 / 右侧 / 俯视',view_prompt='front-right elevated three-quarter, exact SIDE elevation, exact TOP DOWN plan; same whole edible inventory item in all views',scale='统一背包拾取图标尺度与碗具口径；不同菜品可比，无额外展示底座；肉类画切块而非属主动物',style_ref='能源装置/energy_same_scale_overview_v7.png'),
 'equipment':dict(name='装备与饰品',section=15,detail_section=14,prefix='EQP',english='ARMOR & ACCESSORIES',views='正面 / 右侧 / 背面',view_prompt='FRONT view, RIGHT SIDE profile, BACK view of same standalone wearable; all views same size; no human mannequin, no skin, no limbs',scale='统一Roblox块状角色穿戴比例；按胸部/头面/靴/围领分族；无设施底座，不画全套人形',style_ref='sample/ITM-0019_model.png')}

all_records=[]
for key,g in GROUPS.items():
    originals=rows(inventory,g['section']); detail_rows=rows(details,g['detail_section'])
    group=[r for r in R if r['category']==key]
    assert sorted(r['index'] for r in group)==list(range(len(originals))),key
    folder=ROOT/g['name']
    for sub in ['input','versions/v1','final']:(folder/sub).mkdir(parents=True,exist_ok=True)
    for r in group:
        original=originals[r['index']]
        r.update(id=g['prefix']+'-'+str(r['index']+1).zfill(3),original=original[0],original_features=original[2],priority=original[4],source_gdd=original[3])
        r['source_rows']=[]
        for code,num in re.findall(r'([CGEFA])(\d+)',r['refs']):
            cells=catalogs[code][int(num)]
            r['source_rows'].append(dict(file='tmp/'+catalog_files[code],row=int(num),name=cells[2] if code=='F' else cells[1],cells=cells))
        r['status']='调试/占位/预备' if r['rank']==0 or (key=='animals' and r['index'] in [12,13]) or (key=='ranged' and r['index']==4) else '常规/侧支'
        r['images']={'v1':g['name']+'/final/'+r['id']+'_views_v1.png'}
        r['detail_source']=next((d for d in detail_rows if d[0]==r['original']),None)
        all_records.append(r)
    headers=['制品项名称 / 英文 ID','用途与目标','风格参考','主体底面','统一体量','共用交互件','越界规则','示意与简化权限','展示角度','背景','文字与徽标','禁止项','交付与网站']
    values=[g['name']+' / '+key,'替换Roblox原游戏对应素材，保留原ID和用途线索；制作美术方案，不直接修改游戏配置',g['style_ref']+'；机床v2、能源v7（风格参考，不复制机械机构）','不适用设施网格；物品/生物自然轮廓',g['scale'],'无统一投料口；武器握把、装备挂点在同族中统一','允许自然轮廓；不得裁切，不人为加方形台座','允许减少配件，优先1–2识别结构、5–8主要形体；明确标注组合改编',g['views'],'米灰实底、柔和棚光','无水印/文字；毒性/冷却只用克制视觉提示，不添无关阵营徽章','无真实人物、无血腥伤口、无部件制作图、无尺寸加工图、无设施投料管','本目录final与versions；原始PNG图片集包；新增网站独立页面并展示配对与过程']
    text='# '+g['name']+'｜制品输入文档 v1\n\n## 表 A：整套共用规则\n\n| 字段 | 填写内容 |\n| --- | --- |\n'+''.join('| '+a+' | '+b+' |\n' for a,b in zip(headers,values))
    text+='\n## 表 B：全部物体描述表\n\n| 编号 | 等级/分支 | 物体名称 | 功能/技术说明 | 必留结构 | 相比上级提升 | 材质/光效 | 简化/改编 | 特殊约束 |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n'
    for r in group:
        text+='| '+ ' | '.join([r['id'],r['branch']+' / '+str(r['rank']),r['target'],r['original_features'],r['visual'],'同分支按rank比较；0为非成长预留','以visual及设定原文为准，哑光低多边形',r['adaptation'],r['status']+'；原ID/名：'+r['original']])+' |\n'
    text+='\n## 逐项设定依据与视觉转译\n\n'
    for r in group:
        text+='### '+r['id']+' '+r['target']+'\n\n- 原素材：'+r['original']+'；'+r['original_features']+'。\n- 设定引用：'+ '；'.join(s['file']+' #'+str(s['row'])+' '+s['name'] for s in r['source_rows'])+'。\n- 改编与适配：'+r['adaptation']+'。\n- 生图描述：'+r['visual']+'\n\n'
        for s in r['source_rows']: text+='> '+ ' / '.join(s['cells'][1:])+'\n\n'
    (folder/'input/描述表.md').write_text(text)
    (folder/'brief.md').write_text('# '+g['name']+'视觉转译\n\n'+g['scale']+'。\n\n采用同族同尺度、跨族保留自然比例。等级仅在同branch内比较，不能把特殊效果武器、不同生态动物或活动皮肤硬排为一条线。\n\n技术与外观依据见 input/描述表.md；来源和游戏适配见 ../替换对应关系表.md。\n')

out={'schema_version':1,'groups':GROUPS,'records':all_records}
(ROOT/'替换制品登记.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
text='# 原素材 → 废土制品对应关系 v1\n\n## 范围与口径\n\n读取原工程建模素材清单与明细，先阅读废土世界观，再逐项选择图鉴。仅制作美术替换方案，不更改 100daf-rb 原工程配置、数值、命中盒或动画。能源装置对应营火、机床对应制造台沿用既有交付。\n\n本轮83条全部覆盖：动物14、近战18、远程/投掷16、食物19、装备16。包含调试和无配置的预备图；这些不进入正常成长路线。描述表原分类编号与明细表章节编号不同，按名称核对。\n\n## 配对原则\n\n- 分支内先比较原游戏用途/数值，再用素材工艺、动力方式和辨识机构表达成长；不能把霰弹近距伤害200直接解释为全局强于高斯武器。\n- 动物按生态位与威胁度；食物按生熟链/饱食角色；同数值护具按环境分支。rank为本次视觉组织序，不是原游戏新增配置。\n- 无一一对应的效果或造型明确写“改编”，并保留引用；不把原创组合伪装成设定原名。\n- 既有蓝色解毒菇与图鉴蓝伞菇毒性冲突：原毒菇236→有毒蓝伞菇，解毒235→精神叶清凉包的玩法改编，解毒非图鉴原有效果。银嘴蛇不可作为食物，不选图鉴食物表里与生物条目冲突的银嘴蛇肉。\n- 肉类图片画食材切块而非图鉴描述的属主；强化生/熟外观配对。\n- 跨武器类别、跨骨架替换是美术提案，须在Roblox另做动画、投射物、掉落和特效适配，尤其肩托火箭筒、裂爪蟹、双头牛与铁背猿。\n\n## 来源\n\n- 原清单：'+str(ORIGINAL/'建模素材清单.md')+'\n- 原明细：'+str(ORIGINAL/'建模素材明细表.md')+'\n- 世界观：tmp/wasteland_worldview.md\n- 设定行号：以下指图鉴首列序号，并非文件行号。\n'
for key,g in GROUPS.items():
    text+='\n## '+g['name']+'\n\n| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n'
    for r in [r for r in all_records if r['category']==key]:
        text+='| '+' | '.join([r['id'],r['original'],r['original_features'],r['target'],r['branch']+' / '+str(r['rank']),'; '.join(s['file']+' #'+str(s['row'])+' '+s['name'] for s in r['source_rows']),r['adaptation'],r['status']])+' |\n'
(ROOT/'替换对应关系表.md').write_text(text)
with (ROOT/'替换对应关系表.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['编号','分类','原素材','原用途','替换制品','分支','视觉序','来源','适配','状态'])
    for r in all_records:w.writerow([r['id'],GROUPS[r['category']]['name'],r['original'],r['original_features'],r['target'],r['branch'],r['rank'],r['refs'],r['adaptation'],r['status']])
print('Prepared',len(all_records),'source-matched records and',len(GROUPS),'input documents')
