# README

- 项目使用 pydoc-markdown[novella]构建文档、此工具在py3.7及以上运行
- 项目wiki地址：[https://github.com/ASTARCHEN/astartool/wiki](https://github.com/ASTARCHEN/astartool/wiki)
- doc生成命令

```shell
pydoc-markdown -p astar_devopstool > docs/index.md
```

## 注意

- ```docspec_python/__init__.py``` 中 line 121需要插入如下代码,否则代码运行的时候可能因编码报错

```python
  if encoding is None:
    encoding = 'utf-8'
```

- 文档生成不是很全，后面在项目中修改， 主要是__all__里面的识别没对