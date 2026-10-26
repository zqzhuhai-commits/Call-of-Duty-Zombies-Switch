# Call of Duty: Zombies-Switch

基于 NZ:P / Vril 的非官方简体中文 Switch 适配工程。原作团队：NZ:P Team。
这是《使命召唤：僵尸模式》风格的复古自制游戏，不是官方《使命召唤》Switch 移植。

目标：中文菜单与提示、内置游戏资源、最终提供可安装的单文件 NSP。

## 当前状态

- 已编写：222 条显示文本翻译、409 字的中文图集、UTF-8 绘制与文字宽度计算。
- 已编写：RomFS 资源挂载、SD 卡设置/存档读写分离。
- 已通过：桌面端 UTF-8 / 字典 / 字库覆盖测试，修改文件的桌面 C 语法检查。
- 已通过：首次 Switch 交叉编译，NRO 内置约118MB RomFS 资源的结构检查。
- 待验证：中文实机画面、地图加载、设置保存、声音与帧率。
- **尚未完成 NSP。当前没有已验证可玩的中文成品。**
- 当前上游源码禁用合作模式菜单。本工程未实现联机。
- 首批翻译不覆盖动态购买提示、角色长篇介绍、贴图文字或配音。

## 构建

1. 安装 devkitPro Switch 工具链及 `switch-sdl2_mixer`。
2. `python3 tools/prepare.py`：拉取固定引擎提交，应用补丁，下载并校验官方资源包。
3. `bash tools/build-switch.sh`：生成内置 RomFS 的 NRO 和 NSP 后续打包所需 ELF/NACP。

资源包使用 2026-10-22 nightly 的 SHA-256 固定校验。上游 nightly 链接会变动：如果哈希不符，脚本会停止，请先审查新资源再更新，不能跳过校验。
也可传入对应资源 ZIP：`python3 tools/prepare.py --assets-zip /path/to/nzportable-switch.zip`。

`engine/` 是构建工作目录，含本地修改时脚本不会自动覆盖。重新准备前请先保留或移走它。
配置目录为 `sdmc:/switch/nzp-zh/nzp`，无需手动复制游戏素材。NRO 调试时仍须完整内存模式。

## 源码与许可

- 引擎基线：https://github.com/nzp-team/vril-engine/commit/ac0a0ac6b081be3b44e669dafe842b21b2a033d1
- 游戏资源：https://github.com/nzp-team/nzportable/releases/tag/nightly
- 游戏逻辑源码：https://github.com/nzp-team/quakec
- 引擎及对应修改：GPL-2.0-or-later，见 LICENSE 与原文件声明。
- 上游资源：按原资源附带许可保留署名；资源仓库标注 CC BY-SA 4.0。
- 中文字库：Noto Sans SC，SIL OFL 1.1，见 localization/OFL-NotoSansSC.txt。
- 不包含主机密钥。请勿提交 `prod.keys`、个人令牌或其他凭据。

本仓库保存补丁、生成的中文数据及可复现构建脚本；完整引擎源码由固定提交加补丁获得。

## 截图

桌面验证工作流会编译同一中文代码并捕获实际菜单和地图画面，产物名称明确标为 Desktop。它们不是 Switch 实机或模拟器截图，也不代表 Switch 性能。

## NSP 打包准备

`bash tools/prepare-nsp.sh` 将编译好的 ELF 转为应用 NSO，并生成 NPDM、NACP 与图标。
Title ID：`05004E5A505A4800`，配置与普通 NRO 分开保存在 `switch/nzp-zh/`。

最终打包工具采用 hacBrewPack，需要私下提供 `header_key` 和对应的 `key_area_key_application_xx`。
准备好本地工具和密钥文件后运行 `bash tools/pack-nsp.sh /absolute/path/to/prod.keys`。
仓库与自动构建不保存密钥。应用配置仍需实机验证，打包成功不等于已可正常游玩。

## 0.1.1 图标与作者更新

应用显示名：使命召唤：僵尸；作者：Xiao Fan。使用 art/cod-zombies-icon-256.jpg 的新方形图标。
已重新生成 NSP，Title ID 保持 05004E5A505A4800。安装包的程序、控制与元数据校验通过；Switch 实机启动仍未验证。

## 0.1.2 加载方块排查

旧包存在渐进式 JPEG 和语言标记/图标文件不匹配的问题。修正版改为标准 JPEG，并补齐16种语言的图标与支持标记。详见 docs/ICON-FIX-0.1.2.md。
使用 hacBrewPack 打包前应用 packaging/hacbrewpack-v012.patch，提高安装元数据版本号。
这些修正已通过包结构与引用检查，是否解决实机加载方块仍需用户验证。
