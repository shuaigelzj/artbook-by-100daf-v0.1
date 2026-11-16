# 近战武器｜制品输入文档 v1

## 表 A：整套共用规则

| 字段 | 填写内容 |
| --- | --- |
| 制品项名称 / 英文 ID | 近战武器 / melee |
| 用途与目标 | 替换Roblox原游戏对应素材，保留原ID和用途线索；制作美术方案，不直接修改游戏配置 |
| 风格参考 | 机床/machining_same_scale_overview_v2.png；机床v2、能源v7（风格参考，不复制机械机构） |
| 主体底面 | 不适用设施网格；物品/生物自然轮廓 |
| 统一体量 | 统一Roblox握把粗细；短刀/斧/长矛分长度族，不将匕首拉成大剑；无底座 |
| 共用交互件 | 无统一投料口；武器握把、装备挂点在同族中统一 |
| 越界规则 | 允许自然轮廓；不得裁切，不人为加方形台座 |
| 示意与简化权限 | 允许减少配件，优先1–2识别结构、5–8主要形体；明确标注组合改编 |
| 展示角度 | 正视 / 右侧 / 背视 |
| 背景 | 米灰实底、柔和棚光 |
| 文字与徽标 | 无水印/文字；毒性/冷却只用克制视觉提示，不添无关阵营徽章 |
| 禁止项 | 无真实人物、无血腥伤口、无部件制作图、无尺寸加工图、无设施投料管 |
| 交付与网站 | 本目录final与versions；原始PNG图片集包；新增网站独立页面并展示配对与过程 |

## 表 B：全部物体描述表

| 编号 | 等级/分支 | 物体名称 | 功能/技术说明 | 必留结构 | 相比上级提升 | 材质/光效 | 简化/改编 | 特殊约束 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MEL-001 | 调试预留 / 0 | 热熔破拆斧·测试型 | GM 斧，伤害 9999 | Compact tactical breaching axe, dark alloy rectangular head, narrow RED thermal cutting edge, white diagnostic grip band; no lettering. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 管理员伤害9999不进入成长序列；仅测试涂装 | 调试/占位/预备；原ID/名：Admin axe |
| MEL-002 | 采集斧系 / 1 | 废旧木柄伐木斧 | 伤害 10，砍树 1 | Simple worn single-bit iron axe, chipped compact head, curved brown wooden handle bound with coarse rope, no glow. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 将双手伐木斧压缩为新手握持尺度 | 常规/侧支；原ID/名：Old axe（104） |
| MEL-003 | 采集斧系 / 2 | 81号厂战术短斧 | 伤害 20，砍树 3 | Clean forged tactical hatchet, broader grey steel blade and squared hammer poll, straight olive wrapped handle, practical steel collar. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 保留伐木3的进阶角色 | 常规/侧支；原ID/名：Good axe（110） |
| MEL-004 | 刀剑系 / 1 | 战术通用匕首 | 伤害 25 | Short thick matte charcoal survival knife, straight single cutting edge, minimal spine serrations, black rubber grip and small guard; one knife only. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 近身快速副武器 | 常规/侧支；原ID/名：Knife（111） |
| MEL-005 | 刀剑系 / 2 | 军团指挥官军刀 | 伤害 35 | Slightly curved silver military sabre, plain half-basket guard, dark leather grip, restrained bronze pommel; no scabbard. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 长刀替直剑；需挥砍外形适配 | 常规/侧支；原ID/名：Sword（112） |
| MEL-006 | 动力重击 / 4 | 窒息者氮气动力锤 | 伤害 60，雷神锤充能特效 | Two-handed grey power hammer with CYLINDRICAL chamber head, short front impact cone, small blue power cartridge on shaft and one pressure collar, chunky black grip. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 用高压氮气与冷聚变表示原充能重击；不继承雷电神话 | 常规/侧支；原ID/名：Quake（113） |
| MEL-007 | 采集斧系 / 3 | 矛尖长柄战斧 | 伤害 30，砍树 20 | Long steel-handled axe with wide forged chopping blade and one straight TOP spear spike, dark rubber two-handed grip, heavy reinforced collar. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 保留强化采集与长柄两用定位 | 常规/侧支；原ID/名：Power axe（114） |
| MEL-008 | 刀剑系 / 4 | 高频能量护刃直刀 | 伤害 40，能量 10，格挡 | Long solid titanium straight blade with a THIN cyan energized edge, compact battery guard, dark rubber grip; blade is solid metal, not pure light beam. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 实刃加能源护刃为改编；格挡与耗能机制需对接 | 常规/侧支；原ID/名：Light Saber（119） |
| MEL-009 | 采集斧系 / 2.5 | 精锻合金短斧 | 伤害 25，砍树 3，光效 | Precision forged silver-grey hatchet, faceted wedge blade, dark reinforced grip, small non-glowing cyan inspection inset, no crystal blade. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 宝石表现改为精锻合金与状态条；低于长柄采集档 | 常规/侧支；原ID/名：Gem axe（121） |
| MEL-010 | 长柄刺击 / 2 | 合金钢筋投枪 | 伤害 35 | Long rebar-inspired steel spear, polished four-sided spear point, reinforced joint and dark textile mid-grip, no gemstones. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 将宝石矛改为精加工金属尖；本项仍为近战外观 | 常规/侧支；原ID/名：Gem spear（123） |
| MEL-011 | 长柄刺击 / 3 | 银嘴蛇毒猎矛 | 伤害 40，中毒 | Wooden hunting spear with dark metal triangular barbed point, small SEALED green toxin ampoule below tip, leather wrappings, no dripping fluid. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 设定长矛与蛇毒组合改编；保留中毒角色 | 常规/侧支；原ID/名：Poison Spear（125） |
| MEL-012 | 刀剑系 / 2 | 消光潜行战术刀 | 伤害 35 | Long slim matte black tactical knife with subtle recurve edge, compact black guard and dark textured grip, minimal violet metal tint, no magic motifs. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 同伤害35的隐蔽侧支，不假装高于军刀 | 常规/侧支；原ID/名：Night Blade（132） |
| MEL-013 | 控制侧支 / 3 | 低温伺服拳套 | 伤害 20，冰冻减速 | Pair of wearable dark titanium mechanical gauntlets, broad knuckle plates, ONE small cyan coolant cartridge on each forearm cuff, frost-white edge accents; no arms or mannequin. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 机械义肢/手套的低温模块改型；冻结为玩法效果待实现 | 常规/侧支；原ID/名：Glacial Fists（133） |
| MEL-014 | 活动侧支 / 2 | 军官军刀·冬季礼装 | 伤害 35 | Military sabre with same practical half-basket geometry, white metal blade, burgundy leather grip and simple cream cloth tie, no candy-cane or fantasy ornaments. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 圣诞35伤害保持同档；仅冬季涂装 | 常规/侧支；原ID/名：SantaSword（135） |
| MEL-015 | 长柄刺击 / 5 | 氮气动力破甲长枪 | 伤害 100 | Advanced long dark alloy spear, heavy narrow four-sided penetrator tip, cylindrical pressure chamber below tip, small blue energy cell, long black grip; no runes. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 长矛和氮气锤技术组合改编；不是原文独立命名武器 | 常规/侧支；原ID/名：Gungnir（138） |
| MEL-016 | 动力重击 / 5 | 重型高频链锯刃 | 伤害 70 | Two-handed heavy chain blade, broad grey guide bar with TWO rows of large blunt stylized carbide teeth, dark compact motor guard, robust handle; no blood. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 链锯替大剑；需要握持/命中动画适配 | 常规/侧支；原ID/名：Beast Slayer（139） |
| MEL-017 | 采集斧系 / 4 | 工业伐木链锯 | 伤害 30，砍树 40 | Compact yellow industrial chainsaw, thick dark toothed guide bar, top loop handle and rear trigger grip, simple side vents, one machine no loose parts. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 高效连续采集对应砍树40；换为链锯握持 | 常规/侧支；原ID/名：Super Axe（141） |
| MEL-018 | 刀剑系 / 5 | 热熔裁切长刃 | 伤害 60，圣光范围 15 | White-grey tactical long cleaver, solid dark blade with thin warm red-white thermal edge, integrated blocky power guard, subtle amber status bar; no religious symbols. | 同分支按rank比较；0为非成长预留 | 以visual及设定原文为准，哑光低多边形 | 热熔斧技术长刃改型；圣光作用需在玩法中重解释 | 常规/侧支；原ID/名：Holy Sword（147） |

## 逐项设定依据与视觉转译

### MEL-001 热熔破拆斧·测试型

- 原素材：Admin axe；GM 斧，伤害 9999。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”）。
- 改编与适配：管理员伤害9999不进入成长序列；仅测试涂装。
- 生图描述：Compact tactical breaching axe, dark alloy rectangular head, narrow RED thermal cutting edge, white diagnostic grip band; no lettering.

> “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） / 热熔动力战术斧 / 新联盟 / 老白（主力武器） / 高能热熔等离子体 / 弧光切割 / 外观酷似战术消防破拆斧，具有粗犷的暗灰色高强度合金斧身，钝厚的斧背与宽大前斧刃结合。斧柄内置电能接口与导线，启动时斧刃边缘闪烁出猩红色的热熔等离子弧光与高温高频能量流，斧柄配有防滑高分子橡塑护套与战术挂扣。 / 老白抽奖获得并作为招牌武器的高阶破甲冷兵器，能瞬间热熔切开重型陶钢装甲、防空闸门与高阶异种（进化体/圣光骑士团装甲）的硬质外壳。

### MEL-002 废旧木柄伐木斧

- 原素材：Old axe（104）；伤害 10，砍树 1。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #15 伐木斧 / 废土双手大斧。
- 改编与适配：将双手伐木斧压缩为新手握持尺度。
- 生图描述：Simple worn single-bit iron axe, chipped compact head, curved brown wooden handle bound with coarse rope, no glow.

> 伐木斧 / 废土双手大斧 / 农用与伐木双手斧 / 废土农庄 / 玩家 / 淬火高碳钢双刃/单刃斧 / 粗重的大型双刃或单刃伐木斧，配有长达90cm的弯曲山核桃木或硬木斧柄，斧头表面残留着木屑与油脂。 / 玩家撸树开荒、建造营地及遭遇异种浪潮时顺手拿起的强力双手砍劈武器。

### MEL-003 81号厂战术短斧

- 原素材：Good axe（110）；伤害 20，砍树 3。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #12 短斧 / 81号厂战术短斧。
- 改编与适配：保留伐木3的进阶角色。
- 生图描述：Clean forged tactical hatchet, broader grey steel blade and squared hammer poll, straight olive wrapped handle, practical steel collar.

> 短斧 / 81号厂战术短斧 / 单手战术短斧 / 新联盟 / 老白（早期） / 淬火高碳钢斧头 / 锻造斧背 / 斧头由高碳钢淬火锻造，前刃锋利开刃，后斧背呈方头平锤形状，斧柄为50cm长加厚钢管或硬木手柄，柄尾带有防脱手手绳孔。 / 老白等力量系玩家早期与中期的主力近战武器，单手挥砍灵活，斧背可当重锤砸击装甲。

### MEL-004 战术通用匕首

- 原素材：Knife（111）；伤害 25。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首。
- 改编与适配：近身快速副武器。
- 生图描述：Short thick matte charcoal survival knife, straight single cutting edge, minimal spine serrations, black rubber grip and small guard; one knife only.

> 高频/战术通用直刀与匕首 / 战术单兵直刀 / 废土佣兵 / 玩家 / 全贯穿式（Full-tang）厚重刀身 / 25厘米长的厚重高碳钢直刀，刀身表面涂有哑光黑色防锈涂层，刀背带有切削锯齿，刀柄采用带防滑纹路的黑色高分子K胶或橡胶包裹，配有K防脱落战术刀鞘。 / 单兵生存、野外剥皮割肉与近身刺杀的全能冷兵器，废土客与玩家人人必备的随身副武器。

### MEL-005 军团指挥官军刀

- 原素材：Sword（112）；伤害 35。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #10 军团高阶军刀 / 指挥官军刀。
- 改编与适配：长刀替直剑；需挥砍外形适配。
- 生图描述：Slightly curved silver military sabre, plain half-basket guard, dark leather grip, restrained bronze pommel; no scabbard.

> 军团高阶军刀 / 指挥官军刀 / 军官战术长刀 / 军团军官 / 亲卫队 / 80cm 缎面淬火单刃弯刀 / 长约80厘米的单刃微弯军刀，刀身展现出缎面淬火的冷冷金属光泽，配有半封闭式的钢铁防弹护拳手柄，黑皮包钢的军刀鞘挂在腰间，显得庄重威严。 / 军团百夫长及更高阶军官的身份象征与近战战刀，刀身刚柔相济，适合骑马扫砍与军官近身比武。

### MEL-006 窒息者氮气动力锤

- 原素材：Quake（113）；伤害 60，雷神锤充能特效。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #3 窒息者 / 氮气动力锤。
- 改编与适配：用高压氮气与冷聚变表示原充能重击；不继承雷电神话。
- 生图描述：Two-handed grey power hammer with CYLINDRICAL chamber head, short front impact cone, small blue power cartridge on shaft and one pressure collar, chunky black grip.

> 窒息者 / 氮气动力锤 / 氮气动力战术锤 / 新联盟 / 楚光、老白等 / 强力场干涉 / 微型冷聚变电池供电 / 长达一米半的硬质金属锤柄，前段带有枪械式的拉机柄与防滑护木，锤头为一个粗大的圆柱形高压氮气喷射室，前面配有硬质合金破甲锥头；锤柄前段嵌入了一块微型冷聚变电池，闪烁着微弱的淡蓝色荧光。 / 结合枪械与高压氮气的重型战术锤，具备A模式伞状防御（偏移子弹）、B模式氮气装甲接触爆破（类似爆炸冲击波毁伤装甲）与C模式高压喷气加速。

### MEL-007 矛尖长柄战斧

- 原素材：Power axe（114）；伤害 30，砍树 20。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #13 带矛头的长柄斧。
- 改编与适配：保留强化采集与长柄两用定位。
- 生图描述：Long steel-handled axe with wide forged chopping blade and one straight TOP spear spike, dark rubber two-handed grip, heavy reinforced collar.

> 带矛头的长柄斧 / 双手长柄战斧 / 新联盟 / 老白（重装） / 1.2米加厚柄 / 顶端焊接穿刺矛头 / 结合了战斧与长矛的长柄双手武器。1.2米长加厚钢管手柄，前段为宽大锋利的战斧斧刃，顶部延伸出一根长约20cm的四棱重型破甲矛头。 / 老白配备伪·动力装甲时定制的重型长兵器，既可双手破甲大劈大砍，又能居高临下刺穿敌方掩体。

### MEL-008 高频能量护刃直刀

- 原素材：Light Saber（119）；伤害 40，能量 10，格挡。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首；tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”）。
- 改编与适配：实刃加能源护刃为改编；格挡与耗能机制需对接。
- 生图描述：Long solid titanium straight blade with a THIN cyan energized edge, compact battery guard, dark rubber grip; blade is solid metal, not pure light beam.

> 高频/战术通用直刀与匕首 / 战术单兵直刀 / 废土佣兵 / 玩家 / 全贯穿式（Full-tang）厚重刀身 / 25厘米长的厚重高碳钢直刀，刀身表面涂有哑光黑色防锈涂层，刀背带有切削锯齿，刀柄采用带防滑纹路的黑色高分子K胶或橡胶包裹，配有K防脱落战术刀鞘。 / 单兵生存、野外剥皮割肉与近身刺杀的全能冷兵器，废土客与玩家人人必备的随身副武器。

> “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） / 热熔动力战术斧 / 新联盟 / 老白（主力武器） / 高能热熔等离子体 / 弧光切割 / 外观酷似战术消防破拆斧，具有粗犷的暗灰色高强度合金斧身，钝厚的斧背与宽大前斧刃结合。斧柄内置电能接口与导线，启动时斧刃边缘闪烁出猩红色的热熔等离子弧光与高温高频能量流，斧柄配有防滑高分子橡塑护套与战术挂扣。 / 老白抽奖获得并作为招牌武器的高阶破甲冷兵器，能瞬间热熔切开重型陶钢装甲、防空闸门与高阶异种（进化体/圣光骑士团装甲）的硬质外壳。

### MEL-009 精锻合金短斧

- 原素材：Gem axe（121）；伤害 25，砍树 3，光效。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #12 短斧 / 81号厂战术短斧。
- 改编与适配：宝石表现改为精锻合金与状态条；低于长柄采集档。
- 生图描述：Precision forged silver-grey hatchet, faceted wedge blade, dark reinforced grip, small non-glowing cyan inspection inset, no crystal blade.

> 短斧 / 81号厂战术短斧 / 单手战术短斧 / 新联盟 / 老白（早期） / 淬火高碳钢斧头 / 锻造斧背 / 斧头由高碳钢淬火锻造，前刃锋利开刃，后斧背呈方头平锤形状，斧柄为50cm长加厚钢管或硬木手柄，柄尾带有防脱手手绳孔。 / 老白等力量系玩家早期与中期的主力近战武器，单手挥砍灵活，斧背可当重锤砸击装甲。

### MEL-010 合金钢筋投枪

- 原素材：Gem spear（123）；伤害 35。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #23 钢筋标枪 / 磨尖金属投枪。
- 改编与适配：将宝石矛改为精加工金属尖；本项仍为近战外观。
- 生图描述：Long rebar-inspired steel spear, polished four-sided spear point, reinforced joint and dark textile mid-grip, no gemstones.

> 钢筋标枪 / 磨尖金属投枪 / 重型投掷标枪 / 新联盟 / 老白（早期） / 螺纹钢筋/铁管 / 砂轮磨尖四棱枪头 / 由长约1.2至1.5米的加厚螺纹钢筋或厚壁铁管截断，前段在砂轮机上打磨成极其尖锐的圆锥/四棱针尖，尾部缠绕布条以平衡飞行重心。 / 老白等力量系玩家早期杀手锏，依靠强悍肉体力量近距离掷出，可直接穿透变异猪与啃食者。

### MEL-011 银嘴蛇毒猎矛

- 原素材：Poison Spear（125）；伤害 40，中毒。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #24 废土长矛 / 兽骨长枪；tmp/wasteland_creatures_catalog.md #17 银嘴蛇。
- 改编与适配：设定长矛与蛇毒组合改编；保留中毒角色。
- 生图描述：Wooden hunting spear with dark metal triangular barbed point, small SEALED green toxin ampoule below tip, leather wrappings, no dripping fluid.

> 废土长矛 / 兽骨长枪 / 长柄刺杀兵器 / 荒野部落 / 流民 / 2–3米压实木杆 / 磨尖废铁片/兽骨 / 长达两至三米的坚硬变异原木杆，顶端用铁丝与麻绳牢固系结着磨尖的三角废铁片或变异兽骨，枪头下方绑有防血滑手的水刺毛绳。 / 荒野部落与流民防卫营地最基础的长兵器，结阵成矛墙可有效阻挡异种扑杀。

> 银嘴蛇 / 变异毒蛇 / 清泉市东区原始森林 / 身上带有银白色花纹，从唇缝延伸至眼角，毒牙基部能储存120ml剧毒毒液。 / 致命剧毒蛇类，攻击迅捷，毒腺遍布全身无法直接食用。

### MEL-012 消光潜行战术刀

- 原素材：Night Blade（132）；伤害 35。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #9 高频/战术通用直刀与匕首。
- 改编与适配：同伤害35的隐蔽侧支，不假装高于军刀。
- 生图描述：Long slim matte black tactical knife with subtle recurve edge, compact black guard and dark textured grip, minimal violet metal tint, no magic motifs.

> 高频/战术通用直刀与匕首 / 战术单兵直刀 / 废土佣兵 / 玩家 / 全贯穿式（Full-tang）厚重刀身 / 25厘米长的厚重高碳钢直刀，刀身表面涂有哑光黑色防锈涂层，刀背带有切削锯齿，刀柄采用带防滑纹路的黑色高分子K胶或橡胶包裹，配有K防脱落战术刀鞘。 / 单兵生存、野外剥皮割肉与近身刺杀的全能冷兵器，废土客与玩家人人必备的随身副武器。

### MEL-013 低温伺服拳套

- 原素材：Glacial Fists（133）；伤害 20，冰冻减速。
- 设定引用：tmp/personal_equipment_catalog_two_tables.md #46 机械义肢 (战术手臂/腿骨)；tmp/personal_equipment_catalog_two_tables.md #35 耐磨战术手套。
- 改编与适配：机械义肢/手套的低温模块改型；冻结为玩法效果待实现。
- 生图描述：Pair of wearable dark titanium mechanical gauntlets, broad knuckle plates, ONE small cyan coolant cartridge on each forearm cuff, frost-white edge accents; no arms or mannequin.

> 机械义肢 (战术手臂/腿骨) / 人体植入义体 / 巨石城 / 理想城 / 钛合金 / 塑钢 / 伺服电机 / 剥落漆面的钛合金或塑钢机械骨骼，露出的液压管线与伺服电机。 / 替代残肢并提供远超常人的握力、挥击力与奔跑速度。

> 耐磨战术手套 / 防护服与服装 / 废土客 / 佣兵 / 凯夫拉 / 厚橡胶 / 掌心带防滑皮垫，指关节带有硬质防护块。 / 改善枪械握持防滑，防止高热枪管烫伤及手部划伤。

### MEL-014 军官军刀·冬季礼装

- 原素材：SantaSword（135）；伤害 35。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #10 军团高阶军刀 / 指挥官军刀。
- 改编与适配：圣诞35伤害保持同档；仅冬季涂装。
- 生图描述：Military sabre with same practical half-basket geometry, white metal blade, burgundy leather grip and simple cream cloth tie, no candy-cane or fantasy ornaments.

> 军团高阶军刀 / 指挥官军刀 / 军官战术长刀 / 军团军官 / 亲卫队 / 80cm 缎面淬火单刃弯刀 / 长约80厘米的单刃微弯军刀，刀身展现出缎面淬火的冷冷金属光泽，配有半封闭式的钢铁防弹护拳手柄，黑皮包钢的军刀鞘挂在腰间，显得庄重威严。 / 军团百夫长及更高阶军官的身份象征与近战战刀，刀身刚柔相济，适合骑马扫砍与军官近身比武。

### MEL-015 氮气动力破甲长枪

- 原素材：Gungnir（138）；伤害 100。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #24 废土长矛 / 兽骨长枪；tmp/cold_and_powered_weapons_catalog.md #3 窒息者 / 氮气动力锤。
- 改编与适配：长矛和氮气锤技术组合改编；不是原文独立命名武器。
- 生图描述：Advanced long dark alloy spear, heavy narrow four-sided penetrator tip, cylindrical pressure chamber below tip, small blue energy cell, long black grip; no runes.

> 废土长矛 / 兽骨长枪 / 长柄刺杀兵器 / 荒野部落 / 流民 / 2–3米压实木杆 / 磨尖废铁片/兽骨 / 长达两至三米的坚硬变异原木杆，顶端用铁丝与麻绳牢固系结着磨尖的三角废铁片或变异兽骨，枪头下方绑有防血滑手的水刺毛绳。 / 荒野部落与流民防卫营地最基础的长兵器，结阵成矛墙可有效阻挡异种扑杀。

> 窒息者 / 氮气动力锤 / 氮气动力战术锤 / 新联盟 / 楚光、老白等 / 强力场干涉 / 微型冷聚变电池供电 / 长达一米半的硬质金属锤柄，前段带有枪械式的拉机柄与防滑护木，锤头为一个粗大的圆柱形高压氮气喷射室，前面配有硬质合金破甲锥头；锤柄前段嵌入了一块微型冷聚变电池，闪烁着微弱的淡蓝色荧光。 / 结合枪械与高压氮气的重型战术锤，具备A模式伞状防御（偏移子弹）、B模式氮气装甲接触爆破（类似爆炸冲击波毁伤装甲）与C模式高压喷气加速。

### MEL-016 重型高频链锯刃

- 原素材：Beast Slayer（139）；伤害 70。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #5 重型高频链锯（链锯臂）。
- 改编与适配：链锯替大剑；需要握持/命中动画适配。
- 生图描述：Two-handed heavy chain blade, broad grey guide bar with TWO rows of large blunt stylized carbide teeth, dark compact motor guard, robust handle; no blood.

> 重型高频链锯（链锯臂） / 动力装甲/外骨骼链锯 / 军团 / 新联盟 / 黏菌异种 / 柴油/聚变核心驱动 / 双排碳化钨锯齿 / 长达一米至一米半的加厚重型链锯导板，外围环绕着双排粗大的碳化钨硬质合金锯齿，上方带有钢制防溅血护罩与润滑油喷注孔，侧面连接着高速旋转的传动齿轮轴与排气口。 / 挂载于T-10动力装甲或外骨骼右臂，极速旋转的链锯能强行撕裂金属掩体、坚固墙体与重型肉体，近战毁伤效果极其残暴。

### MEL-017 工业伐木链锯

- 原素材：Super Axe（141）；伤害 30，砍树 40。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #6 手持式工业电锯 / 伐木链锯。
- 改编与适配：高效连续采集对应砍树40；换为链锯握持。
- 生图描述：Compact yellow industrial chainsaw, thick dark toothed guide bar, top loop handle and rear trigger grip, simple side vents, one machine no loose parts.

> 手持式工业电锯 / 伐木链锯 / 手持动力锯 / 废土工坊 / 玩家 / 柴油发动机 / 电池驱动 / 亮红色或黄色硬质金属防护外壳，80cm长钢制锯条导板，上方带有前双手横握把与后手柄拉绳启动器，机身侧面带有散热网格与柴油/润滑油加注口。 / 早期伐木与近战突击乱战神器，转速高、锯齿密，在丧尸浪潮近战肉搏中具有极强的威慑力。

### MEL-018 热熔裁切长刃

- 原素材：Holy Sword（147）；伤害 60，圣光范围 15。
- 设定引用：tmp/cold_and_powered_weapons_catalog.md #1 “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”）。
- 改编与适配：热熔斧技术长刃改型；圣光作用需在玩法中重解释。
- 生图描述：White-grey tactical long cleaver, solid dark blade with thin warm red-white thermal edge, integrated blocky power guard, subtle amber status bar; no religious symbols.

> “热熔切割斧”（热熔破拆斧 / 玩家昵称“黑切” / “破甲斧”） / 热熔动力战术斧 / 新联盟 / 老白（主力武器） / 高能热熔等离子体 / 弧光切割 / 外观酷似战术消防破拆斧，具有粗犷的暗灰色高强度合金斧身，钝厚的斧背与宽大前斧刃结合。斧柄内置电能接口与导线，启动时斧刃边缘闪烁出猩红色的热熔等离子弧光与高温高频能量流，斧柄配有防滑高分子橡塑护套与战术挂扣。 / 老白抽奖获得并作为招牌武器的高阶破甲冷兵器，能瞬间热熔切开重型陶钢装甲、防空闸门与高阶异种（进化体/圣光骑士团装甲）的硬质外壳。

