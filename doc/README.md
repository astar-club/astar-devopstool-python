# astar-devopstool 文档 / Documentation

文档按「语言」与「类型」组织：

- 指南文档（手写，按语言分开为独立文件）
  - 中文文档： [README.zh.md](README.zh.md)
  - English documentation: [README.en.md](README.en.md)
- API 参考（由 `pydoc-markdown` 自动生成，按版本归档）
  - 生成说明： [api/README.md](api/README.md)
  - v0.1： [api/v0.1/index.md](api/v0.1/index.md)
  - v0.0.7： [api/v0.0.7/index.md](api/v0.0.7/index.md)
- 版本发布通告
  - v0.1： [version_release/version_release_v0.1.md](version_release/version_release_v0.1.md)
  - v0.0.7： [version_release/version_release_v0.0.7.md](version_release/version_release_v0.0.7.md)

## 文档结构 / Structure

```
doc/
├── README.md                # 本索引文件 / this index
├── README.zh.md             # 中文指南文档
├── README.en.md             # English guide documentation
├── api/                     # 自动生成的 API 参考（pydoc-markdown）
│   ├── README.md
│   ├── v0.1/
│   │   └── index.md
│   └── v0.0.7/
│       └── index.md
└── version_release/         # 版本发布通告
    ├── version_release_v0.1.md
    └── version_release_v0.0.7.md
```
