# CLI 能力地图

这篇文档是 `ChatPPT` CLI 的简明能力地图，用来校对哪些命令已经是一等入口、哪些仍然只是边界或规划。

可导入 Python 函数映射见 [接口树](interface-tree.md)。当前包能力边界见 [能力地图](capability-map.md)。

## 当前 runtime 命令树

以下内容由 `chatppt --tree` 对真实 Click registry 渲染得到。当前 `ChatPPT` 暂无业务子命令，因此只展示 root pseudo-options。

```text
chatppt # chatppt command line interface
├── --help # Show this message and exit
├── --version # Show the package version
└── --tree # Show the registered CLI command tree

```

## 基础入口

```text
chatppt --help           # 验证命令已安装，并查看当前帮助
chatppt --version        # 验证当前安装版本
chatppt --tree           # 输出当前真实 CLI registry
```

## 业务命令状态

当前包还没有业务子命令。新增命令前不要在文档中写模板占位或示例命令作为已实现入口；只有当命令、Python 函数和测试都存在时，才把它写成已实现入口。

## 实现合约

- 每个已实现命令都要能追到 Python 函数、类或 service 层。
- 如果命令会写远端状态，文档必须说明凭据、权限、dry-run/checkpoint 或确认边界。
- 新增命令时，同步更新 README、接口树、能力地图、测试和相关 Flow 页面。
