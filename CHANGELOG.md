# Changelog

## 2026-08-22

### Changed

- 发布 `ChatPPT` patch `0.1.2`，将本地 Click tree renderer 迁移到 ChatStyle `add_tree_option()`，并新增 registry-backed `chatppt --tree-brief`。
- 将运行时基线对齐到 `chatstyle>=0.2.0,<0.3.0` 和 `chatenv>=0.2.10,<0.3.0`，保留 typed ChatEnv provider 与 ChatEnv 管理的 profile 存储路径。
- 扩展 Python 3.10-3.12 CI、安装态 CLI/ChatEnv 与 wheel smoke、构建/Twine 检查，并为 tag 发布增加默认分支祖先校验。

## 2026-08-11

### Added

- 发布 `ChatPPT` patch `0.1.1`，新增真实 Click registry 生成的顶层 `chatppt --tree`。
- CLI 树文档现在记录当前真实空业务命令面，只展示 root pseudo-options，不再保留模板占位。

### Changed

- 将 ChatEnv 依赖下界提升到已发布 rollout 基线 `>=0.2.4,<0.3.0`。
- 将 MkDocs Material 文档依赖收紧到当前 strict-build 验证窗口。

## 2026-08-06

### Added

- 发布 ChatPPT 首个工作流验证版本 `0.1.0`，包含 ChatArch Python 包基础 CLI、ChatEnv provider、测试、MkDocs 文档站 scaffold 与 PyPI Trusted Publisher 发布工作流。
