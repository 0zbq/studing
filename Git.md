Git的本质上就是一个存档工具。

Git的相关：GitHub，VScode

官方教材：([Git Pro](https://git-scm.com/book/zh/v2))

Git的相关概念：

​	本地仓库：.git文件		远端仓库：GitHub上的仓库

​	多人协作：分支，合并，推送规则，审查

​	提交：commit ，push

​	Git配置文件：.gitignore



提交规范：

配合vscode插件使用

[约定式提交](https://www.conventionalcommits.org/zh-hans/v1.0.0/)

原文：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

译文：

```
<类型>[可选 范围]: <描述>

[可选 正文]

[可选 脚注]
```

------

例如 `feat(parser): adds ability to parse arrays.`。