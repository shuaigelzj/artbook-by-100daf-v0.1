# 原素材 → 废土制品对应关系 v1

## 范围与口径

读取原工程建模素材清单与明细，先阅读废土世界观，再逐项选择图鉴。仅制作美术替换方案，不更改 100daf-rb 原工程配置、数值、命中盒或动画。能源装置对应营火、机床对应制造台沿用既有交付。

本轮83条全部覆盖：动物14、近战18、远程/投掷16、食物19、装备16。包含调试和无配置的预备图；这些不进入正常成长路线。描述表原分类编号与明细表章节编号不同，按名称核对。

## 配对原则

- 分支内先比较原游戏用途/数值，再用素材工艺、动力方式和辨识机构表达成长；不能把霰弹近距伤害200直接解释为全局强于高斯武器。
- 动物按生态位与威胁度；食物按生熟链/饱食角色；同数值护具按环境分支。rank为本次视觉组织序，不是原游戏新增配置。
- 无一一对应的效果或造型明确写“改编”，并保留引用；不把原创组合伪装成设定原名。
- 既有蓝色解毒菇与图鉴蓝伞菇毒性冲突：原毒菇236→有毒蓝伞菇，解毒235→精神叶清凉包的玩法改编，解毒非图鉴原有效果。银嘴蛇不可作为食物，不选图鉴食物表里与生物条目冲突的银嘴蛇肉。
- 肉类图片画食材切块而非图鉴描述的属主；强化生/熟外观配对。
- 跨武器类别、跨骨架替换是美术提案，须在Roblox另做动画、投射物、掉落和特效适配，尤其肩托火箭筒、裂爪蟹、双头牛与铁背猿。

## 来源

- 原清单：/Users/lzj/vibegame/100daf-rb/modeling-assets/建模素材清单.md
- 原明细：/Users/lzj/vibegame/100daf-rb/modeling-assets/建模素材明细表.md
- 世界观：tmp/wasteland_worldview.md
- 设定行号：以下指图鉴首列序号，并非文件行号。

## 动物

| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ANI-001 | Baby Wolf | HP100，zone2，可驯服 | 幼年变异鬣狗 | 荒野主线 / 1 | tmp/wasteland_creatures_catalog.md #7 变异鬣狗 (双头鬣狗) | 幼体改编；保留早期可驯服生态位 | 常规/侧支 |
| ANI-002 | Wolf | HP100，zone3，可驯服 | 双头变异鬣狗 | 荒野主线 / 2 | tmp/wasteland_creatures_catalog.md #7 变异鬣狗 (双头鬣狗) | 选用设定中的双头变体；需双头骨架 | 常规/侧支 |
| ANI-003 | Bear | HP250，zone4，可驯服 | 妖怪·林地型 | 荒野主线 / 3 | tmp/wasteland_creatures_catalog.md #2 妖怪 (变异棕熊/雪熊) | 变异熊轮廓；腐烂改为无血腥硬皮斑块 | 常规/侧支 |
| ANI-004 | Cougar | HP350，zone5，可驯服 | 铁背猿 | 荒野主线 / 4 | tmp/wasteland_creatures_catalog.md #3 铁背猿 | 以智慧异种替代高速猫科；需新攀行/近战骨架 | 常规/侧支 |
| ANI-005 | Mad Bear | HP450，zone6，狂暴熊 | 死亡之爪 | 荒野主线 / 5 | tmp/wasteland_creatures_catalog.md #1 死亡之爪 (死爪) | 压缩原著巨型体量为后期精英兽；不声称沿用熊骨架 | 常规/侧支 |
| ANI-006 | Wild Boar | HP100，沼泽，可驯服 | 变异野猪 | 湿地主线 / 1 | tmp/wasteland_creatures_catalog.md #8 变异野猪 | 保持野猪冲撞与召唤小怪复用 | 常规/侧支 |
| ANI-007 | Alligator | HP250，沼泽 | 裂爪蟹 | 湿地主线 / 2 | tmp/wasteland_creatures_catalog.md #13 裂爪蟹 | 蟹替鳄鱼；需八足/双钳骨架和碰撞适配 | 常规/侧支 |
| ANI-008 | Turkey | HP150，沼泽/感恩节 | 黑鸟·地栖型 | 湿地采猎 / 1 | tmp/wasteland_creatures_catalog.md #31 黑鸟 (变异乌鸦) | 将巨大黑鸟改为落地采猎禽；是否飞行另配 | 常规/侧支 |
| ANI-009 | Snow Wolf | HP125，雪原 | 变异雪狼 | 雪原主线 / 2 | tmp/wasteland_creatures_catalog.md #11 变异雪狼 (雪狼) | 雪地分支；非全物种科技升级 | 常规/侧支 |
| ANI-010 | Snow bear | HP250，雪原 | 妖怪·雪原型 | 雪原主线 / 3 | tmp/wasteland_creatures_catalog.md #2 妖怪 (变异棕熊/雪熊) | 同源雪熊改型；毛色与保暖结构适配 | 常规/侧支 |
| ANI-011 | Bunny（BunnyModel） | 不攻击，受击逃跑，掉兔脚 | 变异松鼠 | 温顺采猎 / 1 | tmp/wasteland_creatures_catalog.md #35 变异松鼠 | 保留兔子的受击逃跑角色；兔脚掉落需改名 | 常规/侧支 |
| ANI-012 | Buffalo（301） | 温顺动物，雪原，不掉皮 | 双头牛 | 温顺采猎 / 3 | tmp/wasteland_creatures_catalog.md #5 双头牛 | 温顺驮兽；双头与原水牛骨架不同 | 常规/侧支 |
| ANI-013 | Elk | 仅预制体，无配置，疑废弃 | 大角鹿 | 温顺采猎 / 2 | tmp/wasteland_creatures_catalog.md #6 角鹿 (大角鹿) | 原仅预制体；预备资产不接入主线 | 调试/占位/预备 |
| ANI-014 | Snow Leopard | 仅预制体，无配置 | 穴居兽·霜灰型 | 雪原预备 / 4 | tmp/wasteland_creatures_catalog.md #12 穴居兽 | 原仅预制体；穴居兽霜灰配色为适应性改编 | 调试/占位/预备 |

## 近战武器

| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MEL-001 | Admin axe | GM 斧，伤害 9999 | 热熔破拆斧·测试型 | 调试预留 / 0 | tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） | 管理员伤害9999不进入成长序列；仅测试涂装 | 调试/占位/预备 |
| MEL-002 | Old axe（104） | 伤害 10，砍树 1 | 废旧木柄伐木斧 | 采集斧系 / 1 | tmp/cold_and_powered_weapons_catalog.md #15 伐木斧 / 废土双手大斧 | 将双手伐木斧压缩为新手握持尺度 | 常规/侧支 |
| MEL-003 | Good axe（110） | 伤害 20，砍树 3 | 81号厂战术短斧 | 采集斧系 / 2 | tmp/cold_and_powered_weapons_catalog.md #12 短斧 / 81号厂战术短斧 | 保留伐木3的进阶角色 | 常规/侧支 |
| MEL-004 | Knife（111） | 伤害 25 | 战术通用匕首 | 刀剑系 / 1 | tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首 | 近身快速副武器 | 常规/侧支 |
| MEL-005 | Sword（112） | 伤害 35 | 军团指挥官军刀 | 刀剑系 / 2 | tmp/cold_and_powered_weapons_catalog.md #10 军团高阶军刀 / 指挥官军刀 | 长刀替直剑；需挥砍外形适配 | 常规/侧支 |
| MEL-006 | Quake（113） | 伤害 60，雷神锤充能特效 | 窒息者氮气动力锤 | 动力重击 / 4 | tmp/cold_and_powered_weapons_catalog.md #3 窒息者 / 氮气动力锤 | 用高压氮气与冷聚变表示原充能重击；不继承雷电神话 | 常规/侧支 |
| MEL-007 | Power axe（114） | 伤害 30，砍树 20 | 矛尖长柄战斧 | 采集斧系 / 3 | tmp/cold_and_powered_weapons_catalog.md #13 带矛头的长柄斧 | 保留强化采集与长柄两用定位 | 常规/侧支 |
| MEL-008 | Light Saber（119） | 伤害 40，能量 10，格挡 | 高频能量护刃直刀 | 刀剑系 / 4 | tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首; tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） | 实刃加能源护刃为改编；格挡与耗能机制需对接 | 常规/侧支 |
| MEL-009 | Gem axe（121） | 伤害 25，砍树 3，光效 | 精锻合金短斧 | 采集斧系 / 2.5 | tmp/cold_and_powered_weapons_catalog.md #12 短斧 / 81号厂战术短斧 | 宝石表现改为精锻合金与状态条；低于长柄采集档 | 常规/侧支 |
| MEL-010 | Gem spear（123） | 伤害 35 | 合金钢筋投枪 | 长柄刺击 / 2 | tmp/cold_and_powered_weapons_catalog.md #23 钢筋标枪 / 磨尖金属投枪 | 将宝石矛改为精加工金属尖；本项仍为近战外观 | 常规/侧支 |
| MEL-011 | Poison Spear（125） | 伤害 40，中毒 | 银嘴蛇毒猎矛 | 长柄刺击 / 3 | tmp/cold_and_powered_weapons_catalog.md #24 废土长矛 / 兽骨长枪; tmp/wasteland_creatures_catalog.md #17 银嘴蛇 | 设定长矛与蛇毒组合改编；保留中毒角色 | 常规/侧支 |
| MEL-012 | Night Blade（132） | 伤害 35 | 消光潜行战术刀 | 刀剑系 / 2 | tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首 | 同伤害35的隐蔽侧支，不假装高于军刀 | 常规/侧支 |
| MEL-013 | Glacial Fists（133） | 伤害 20，冰冻减速 | 低温伺服拳套 | 控制侧支 / 3 | tmp/personal_equipment_catalog_two_tables.md #46 机械义肢 (战术手臂/腿骨); tmp/personal_equipment_catalog_two_tables.md #35 耐磨战术手套 | 机械义肢/手套的低温模块改型；冻结为玩法效果待实现 | 常规/侧支 |
| MEL-014 | SantaSword（135） | 伤害 35 | 军官军刀·冬季礼装 | 活动侧支 / 2 | tmp/cold_and_powered_weapons_catalog.md #10 军团高阶军刀 / 指挥官军刀 | 圣诞35伤害保持同档；仅冬季涂装 | 常规/侧支 |
| MEL-015 | Gungnir（138） | 伤害 100 | 氮气动力破甲长枪 | 长柄刺击 / 5 | tmp/cold_and_powered_weapons_catalog.md #24 废土长矛 / 兽骨长枪; tmp/cold_and_powered_weapons_catalog.md #3 窒息者 / 氮气动力锤 | 长矛和氮气锤技术组合改编；不是原文独立命名武器 | 常规/侧支 |
| MEL-016 | Beast Slayer（139） | 伤害 70 | 重型高频链锯刃 | 动力重击 / 5 | tmp/cold_and_powered_weapons_catalog.md #5 重型高频链锯（链锯臂） | 链锯替大剑；需要握持/命中动画适配 | 常规/侧支 |
| MEL-017 | Super Axe（141） | 伤害 30，砍树 40 | 工业伐木链锯 | 采集斧系 / 4 | tmp/cold_and_powered_weapons_catalog.md #6 手持式工业电锯 / 伐木链锯 | 高效连续采集对应砍树40；换为链锯握持 | 常规/侧支 |
| MEL-018 | Holy Sword（147） | 伤害 60，圣光范围 15 | 热熔裁切长刃 | 刀剑系 / 5 | tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） | 热熔斧技术长刃改型；圣光作用需在玩法中重解释 | 常规/侧支 |

## 远程与投掷武器

| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RNG-001 | Toy Gun（600） | 伤害 100，弹匣 9999，疑似调试 | 警用电击枪·测试型 | 调试预留 / 0 | tmp/firearms_and_weapons_catalog.md #6 警用电击枪 | 9999弹匣仅调试；不作为威力排名 | 调试/占位/预备 |
| RNG-002 | Revolver（601） | 伤害 40，6 发 | 传统转轮手枪 | 手枪主线 / 1 | tmp/firearms_and_weapons_catalog.md #5 传统左轮手枪 | 保持基础6发副武器 | 常规/侧支 |
| RNG-003 | Rifle（602） | 伤害 100，2 发 | 栓动铁管步枪 | 长枪主线 / 1 | tmp/firearms_and_weapons_catalog.md #16 9mm 栓动式铁管步枪 | 保留早期慢射步枪定位 | 常规/侧支 |
| RNG-004 | Shotgun（603） | 伤害 200，2 发 | 双管猎枪 | 近距爆发 / 2 | tmp/firearms_and_weapons_catalog.md #27 双管猎枪 / 霰弹枪 | 保留两发霰弹结构 | 常规/侧支 |
| RNG-005 | SAM Rifle（604） | 无预制体/无配置，仅配置 | 高斯精确狙击步枪 | 长枪预备 / 5 | tmp/firearms_and_weapons_catalog.md #31 电磁 / 高斯狙击步枪 | 原无预制体与明确参数；只预备美术不推断伤害 | 调试/占位/预备 |
| RNG-006 | Toxic Bow（605） | 伤害 70，中毒 | 蛇毒木猎弓 | 弓系 / 1 | tmp/cold_and_powered_weapons_catalog.md #20 废土木猎弓 / 竹木长弓; tmp/wasteland_creatures_catalog.md #17 银嘴蛇 | 猎弓加封装毒箭为组合改编 | 常规/侧支 |
| RNG-007 | Molotov（606） | 爆炸 50，燃烧 | 废土燃烧投掷瓶 | 投掷系 / 1 | tmp/wasteland_creatures_catalog.md #3 铁背猿 | 铁背猿条目提及燃烧瓶；瓶体具体外观为游戏化补全 | 常规/侧支 |
| RNG-008 | Gatling（607） | 10×15，弹匣 504 | 联合收割机轻机枪 | 持续火力 / 4 | tmp/firearms_and_weapons_catalog.md #28 LD-47j “联合收割机” | 以弹鼓轻机枪代替加特林；射速/弹药动画需适配 | 常规/侧支 |
| RNG-009 | Bomb（608） | 伤害 100，半径 30 | 地精肩托火箭筒 | 范围重火力 / 3 | tmp/firearms_and_weapons_catalog.md #34 地精火箭筒 / RPG-7 | 炸弹改为肩托火箭筒；须新增肩扛动画和飞行爆炸投射物 | 常规/侧支 |
| RNG-010 | Peacekeeper Revolver（609） | 伤害 80，8 发 | 银蛇精密左轮 | 手枪主线 / 2 | tmp/firearms_and_weapons_catalog.md #4 “银蛇”左轮手枪 | 精装副武器对应伤害80；弹巢规格按游戏配置适配 | 常规/侧支 |
| RNG-011 | Ice Bow（610） | 伤害 70，冰冻 | 破晓机械复合弓·低温箭型 | 弓系 / 3 | tmp/cold_and_powered_weapons_catalog.md #2 “破晓”机械复合弓 | 电驱弓原文；低温箭头为控制玩法改编 | 常规/侧支 |
| RNG-012 | Four-Barrel Pistol（611） | 30/发，12 发 | Pu-9紧凑冲锋枪 | 自动手枪侧支 / 3 | tmp/firearms_and_weapons_catalog.md #24 Pu-9 冲锋枪 | 替换四管手枪；连发方式和握持须适配 | 常规/侧支 |
| RNG-013 | Reusable Molotov（613） | 可复用燃烧瓶，容量 5→10 | 旋风转轮榴弹发射器 | 范围重火力 / 4 | tmp/firearms_and_weapons_catalog.md #35 “旋风” / “火龙果”榴弹发 | 可复用燃烧瓶改为可补给多发发射器；非自动继承原逻辑 | 常规/侧支 |
| RNG-014 | Boilerheart Revolver（614） | 伤害 110，蒸汽左轮 | 黑天鹅G9无托步枪 | 自动火力 / 4 | tmp/firearms_and_weapons_catalog.md #12 “黑天鹅”G9 突击步枪 | 原蒸汽左轮升级为企业步枪；动画/射击频率需调整 | 常规/侧支 |
| RNG-015 | Iron Verdict Rifle（615） | 伤害 180，穿透 4，射程 300 | 15式刺针高斯步枪 | 长枪主线 / 5 | tmp/firearms_and_weapons_catalog.md #30 15式“刺针”高斯步枪 | 终极工坊产物以电磁技术表达；三部件拆装需新模块 | 常规/侧支 |
| RNG-016 | Holy Water（612） | 伤害 100/150，可伤幽灵 | 火炬心灵干涉投掷罐 | 特殊控制 / 4 | tmp/personal_equipment_catalog_two_tables.md #41 “火炬”心灵干涉仪 | 银白扣件放大为投掷罐的组合改型；幽灵改题材效果需开发 | 常规/侧支 |

## 食物

| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FOD-001 | 216 Carrot | 饱食 15 | 羊角薯 | 基础采集 / 1 | tmp/wasteland_food_and_ingredients.md #1 羊角薯 | 替代胡萝卜；同为低阶块根 | 常规/侧支 |
| FOD-002 | 217 Meat | 饱食 15，烧烤→224 | 鬣狗生肉块 | 普通肉生熟链 / 1 | tmp/wasteland_food_and_ingredients.md #18 变异鬣狗肉 | 食材图画切块而非原文属主动物 | 常规/侧支 |
| FOD-003 | 218 Soup | 饱食 100 | 菌菇薯泥炖汤 | 汤品支线 / 3 | tmp/wasteland_food_and_ingredients.md #10 野生松茸 / 变异平菇; tmp/wasteland_food_and_ingredients.md #52 羊角薯泥 / 土豆泥 | 设定食材组合成汤为菜谱改编；饱食100保留为原参数 | 常规/侧支 |
| FOD-004 | 221 Steak | 饱食 20，烧烤→225 | 双头牛生牛排 | 牛排生熟链 / 1 | tmp/wasteland_food_and_ingredients.md #17 双头牛肉 | 来源双头牛，图为切片不是双头动物 | 常规/侧支 |
| FOD-005 | 224 Cooked Meat | 饱食 30，缺预制体 | 炭烤鬣狗肉 | 普通肉生熟链 / 2 | tmp/wasteland_food_and_ingredients.md #18 变异鬣狗肉; tmp/wasteland_food_and_ingredients.md #46 风干肉 / 腊肉 / 熏肉 | 217→224沿用肉块轮廓与脂肪位置 | 常规/侧支 |
| FOD-006 | 225 Cooked Steak | 饱食 40，缺预制体 | 黄油烤双头牛牛排 | 牛排生熟链 / 2 | tmp/wasteland_food_and_ingredients.md #17 双头牛肉; tmp/wasteland_food_and_ingredients.md #35 黄油 | 221→225保留牛排截面形状 | 常规/侧支 |
| FOD-007 | 226 Perfect Soup | 饱食 120 | 松子鲜鱼汤 | 汤品支线 / 4 | tmp/wasteland_food_and_ingredients.md #14 松子; tmp/wasteland_food_and_ingredients.md #28 水水鱼肉 | 优质汤配方，资料中有明确菜名 | 常规/侧支 |
| FOD-008 | 231 Pumpkin | 饱食 100 | 变异玉米棒 | 高能作物 / 2 | tmp/wasteland_food_and_ingredients.md #3 变异玉米 | 替代南瓜；饱食100沿用原游戏不归因真实营养 | 常规/侧支 |
| FOD-009 | 232 Watermelon | 饱食 100 | 变异椰果 | 高能作物 / 2 | tmp/wasteland_food_and_ingredients.md #15 椰子 / 变异椰果 | 替代西瓜；补水与食用定位 | 常规/侧支 |
| FOD-010 | 234 Red Mushroom | 饱食 15，烧烤→237 | 野生松茸 | 菌菇采集链 / 1 | tmp/wasteland_food_and_ingredients.md #10 野生松茸 / 变异平菇 | 安全可食用菇替红菇；配色不代表真实食用判断 | 常规/侧支 |
| FOD-011 | 235 Blue Mushroom | 解毒 | 精神叶清凉包 | 特殊补给 / 2 | tmp/wasteland_food_and_ingredients.md #12 精神叶 | 精神叶只记提神镇静；解毒效果为游戏化改编而非原文事实 | 常规/侧支 |
| FOD-012 | 236 Green Mushroom | 有毒 | 蓝伞菇 | 有毒资源 / 1 | tmp/wasteland_food_and_ingredients.md #9 蓝伞菇 (蓝色天使) | 蓝色天使在设定中有毒；明确不与原解毒蓝菇混淆 | 常规/侧支 |
| FOD-013 | 237 Roasted Mushrooms | 饱食 30，缺预制体 | 炭烤松茸串 | 菌菇采集链 / 2 | tmp/wasteland_food_and_ingredients.md #10 野生松茸 / 变异平菇 | 234→237视觉生熟；其他菇转换须单独审查 | 常规/侧支 |
| FOD-014 | 238 TomatoSoup | 饱食 120 | 裂爪蟹肉浓汤 | 汤品支线 / 4 | tmp/wasteland_food_and_ingredients.md #27 裂爪蟹肉与蟹黄 | 番茄汤改为高级水产汤，配方为改编 | 常规/侧支 |
| FOD-015 | 239 Turkey | 饱食 40，烧烤→240 | 黑鸟鲜禽肉 | 禽肉生熟链 / 1 | tmp/wasteland_food_and_ingredients.md #24 变异鸟肉 / 鸟蛋 | 239→240用鸟肉截块；不复刻乌鸦整只外观 | 常规/侧支 |
| FOD-016 | 240 Roast Turkey | 饱食 80，缺预制体 | 柴火烤黑鸟肉 | 禽肉生熟链 / 2 | tmp/wasteland_food_and_ingredients.md #24 变异鸟肉 / 鸟蛋 | 保持239→240同轮廓 | 常规/侧支 |
| FOD-017 | 242 Turkey | 饱食 40，重名 | 妖怪上等生肉 | 高热肉生熟链 / 1 | tmp/wasteland_food_and_ingredients.md #23 妖怪肉 | 242→243以大块高热异种肉代替重复火鸡 | 常规/侧支 |
| FOD-018 | 243 Roast Turkey | 饱食 120，缺预制体 | 蜜烤妖怪肉 | 高热肉生熟链 / 3 | tmp/wasteland_food_and_ingredients.md #23 妖怪肉; tmp/wasteland_food_and_ingredients.md #46 风干肉 / 腊肉 / 熏肉 | 高饱食120由精制烹饪表达，不冒充真科技升级 | 常规/侧支 |
| FOD-019 | 245 Warm fruit | 饱食 7，保暖向 | 烘暖卡姆果 | 特殊补给 / 1 | tmp/wasteland_food_and_ingredients.md #5 卡姆果 (卡姆树果实) | 暖果改编；保暖来自加工状态，不声称原果自发热 | 常规/侧支 |

## 装备与饰品

| 编号 | 原素材 | 原用途/参数线索 | 废土替换 | 分支/视觉序 | 图鉴依据 | 适配与改编 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EQP-001 | Admin shoe（1） | GM 护甲 50 | 龙骑兵助推靴·测试型 | 调试预留 / 0 | tmp/personal_equipment_catalog_two_tables.md #3 OD-10 “龙骑兵”动力装甲 | 管理员护甲50仅调试；只画靴子不画全装甲 | 调试/占位/预备 |
| EQP-002 | 301 Leather Armor | 护甲 2 | 变异兽皮护胸 | 护胸主线 / 1 | tmp/personal_equipment_catalog_two_tables.md #21 变异兽皮护甲 | 原护甲2；保留胸部可穿戴边界 | 常规/侧支 |
| EQP-003 | 302 Iron Armor | 护甲 5 | 军团合金胸甲 | 护胸主线 / 2 | tmp/personal_equipment_catalog_two_tables.md #20 军团军官防弹胸甲 | 原护甲5；板片式防护 | 常规/侧支 |
| EQP-004 | 303 Gilded Armor | 护甲 8 | T-10陶钢动力护胸 | 护胸主线 / 5 | tmp/personal_equipment_catalog_two_tables.md #1 T-10 动力装甲 | 原护甲8；从全套动力甲提取胸背组件，不增加完整四肢 | 常规/侧支 |
| EQP-005 | 304 Gilded Breastplate | 护甲 999，占位 | 黄金特装护胸·预备型 | 占位预留 / 0 | tmp/personal_equipment_catalog_two_tables.md #9 “黄金”特装动力装甲 | 原护甲999占位不进入正式强度序列 | 调试/占位/预备 |
| EQP-006 | 305 Gem Armor | 护甲 7 | 高分子陶钢防弹胸甲 | 护胸主线 / 4 | tmp/personal_equipment_catalog_two_tables.md #18 高分子陶钢防弹胸甲 | 原护甲7；高于几丁质6，低于动力护胸8 | 常规/侧支 |
| EQP-007 | 306 Bandit Mask | 护甲 4 | 战术防尘风镜面罩 | 面部防护 / 1 | tmp/personal_equipment_catalog_two_tables.md #34 战术防尘风镜 | 原护甲4；风镜加下半脸布罩的游戏化组合 | 常规/侧支 |
| EQP-008 | 307 Bird Beak Mask | 护甲 8 | 双滤罐防毒面具 | 面部防护 / 2 | tmp/personal_equipment_catalog_two_tables.md #33 全脸防毒面具 | 原护甲8；双滤罐取代鸟嘴造型 | 常规/侧支 |
| EQP-009 | 308 Cowboy Boots | 护甲 3 | 防刺战术军靴 | 足部防护 / 1 | tmp/personal_equipment_catalog_two_tables.md #36 防刺战术军靴 | 原护甲3；保留成对靴件 | 常规/侧支 |
| EQP-010 | 309 Swampscale Breastplate | 护甲 6 | 裂爪蟹几丁质护胸 | 护胸主线 / 3 | tmp/personal_equipment_catalog_two_tables.md #22 几丁质硬壳防具 | 原护甲6；甲壳取代鳄鱼鳞片 | 常规/侧支 |
| EQP-011 | 310 Sheep Head Mask | 护甲 8 | 密封防辐射头罩 | 面部防护 / 2 | tmp/personal_equipment_catalog_two_tables.md #26 全密封防辐射服 / 防化服 | 原护甲8；提取头罩替羊头面罩，非整套连体服 | 常规/侧支 |
| EQP-012 | 311 Thor's Armor | 护甲 8 | 重骑兵外骨骼护胸 | 护胸主线 / 4.5 | tmp/personal_equipment_catalog_two_tables.md #13 六式“重骑兵”警用外骨骼 | 原护甲8同档侧支；仅胸背伺服结构，不画整副机架 | 常规/侧支 |
| EQP-013 | 312 Scarf V1 | 减伤 0.2 | 粗布遮风围领 | 颈部防护 / 1 | tmp/personal_equipment_catalog_two_tables.md #29 废土粗布/皮质遮风斗篷 | 斗篷裁成颈部围领；保留减伤0.2角色 | 常规/侧支 |
| EQP-014 | 313 Scarf V2 | 减伤 0.37 | 魔鬼丝防弹围领 | 颈部防护 / 2 | tmp/personal_equipment_catalog_two_tables.md #28 魔鬼丝战术防弹斗篷 | 防弹斗篷改成围领；对应减伤0.37 | 常规/侧支 |
| EQP-015 | 314 Ice Armor | 护甲 8 | 海狮密封护胸 | 环境护胸侧支 / 5 | tmp/personal_equipment_catalog_two_tables.md #4 “海狮”两栖动力装甲 | 原护甲8同档环境分支；只提取胸背水密组件 | 常规/侧支 |
| EQP-016 | 315 Santa Armor | 护甲 7 | 先锋冬季战术护胸 | 活动护胸侧支 / 4 | tmp/personal_equipment_catalog_two_tables.md #16 “先锋 I 型”军用外骨骼; tmp/personal_equipment_catalog_two_tables.md #31 变异兽皮大衣 | 原护甲7；冬季皮草为适配改编，不假装高于T-10 | 常规/侧支 |
