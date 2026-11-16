# 废土造物 · 制品交付档案

静态网站，无运行依赖。入口 `dist/index.html`，共七个独立制品页：能源装置、机床、动物、近战、远程/投掷、食物、装备/饰品。

本轮新增 83 件概念设计。各页包含风格母图、单件三视图、按原名/新名/编号搜索、支线筛选、原素材配对、出处与改编、实际制作记录、文档和原 PNG 集下载。能源 v1–v7 与机床 v1–v2 历史及逐件版本对比继续保留。新增五组是首轮 v1，暂不虚构第二轮比较。

## 更新

`catalog.json` 定义分组元数据、版本说明与源图映射；`build.py` 读取数据、生成 WebP、复制文档和分组原图 ZIP、生成独立页面。导航自动根据数据生成。

在工程根目录执行：

```sh
python3 tools/package_replacements.py
python3 showcase-site/build.py
python3 showcase-site/verify.py
osascript -l JavaScript showcase-site/verify.js
```

构建依赖 Pillow；最后一条是 macOS JXA 的 DOM 模拟交互检查，不是真实浏览器测试。原始 PNG 不受 WebP 转换影响。

`废土造物-展示网站.zip` 包含完整 `dist/`，解压后直接打开首页，可离线交给同事。网站不包含在线审批、账号或评论功能。

## 发布与验证边界

当前环境没有 Node，先前网络代理不可连接，不能运行 Sites 源码同步与发布助手。已复查现有私有 Sites：尚无在线发布版本；项目身份仍保存在 `.openai/hosting.json`，后续必须复用，不要重新创建。当前交付是本地更新和离线压缩包，没有声称更新线上站点。

图片和文档完整性、页面路由、数据覆盖、搜索筛选与已有版本对比使用静态/JXA 检查。当前环境未进行真实浏览器排版和移动端视觉验证。
