# Git 入门笔记

## git init

作用：在当前目录创建一个新的 Git 仓库。

示例：

```bash
git init
```

## git add

作用：把文件加入暂存区，准备提交。

示例：

```bash
git add README.md
git add .
```

## git commit

作用：把暂存区内容保存为一次提交。

示例：

```bash
git commit -m "docs: add git notes"
```

## git status

作用：查看哪些文件被修改、哪些文件已暂存。

示例：

```bash
git status
```

## git log

作用：查看提交历史。

示例：

```bash
git log
git log --oneline
```

## git branch

作用：查看、创建或切换分支。

示例：

```bash
git branch
git branch feature-notes
```

## git remote

作用：管理远端仓库地址。

示例：

```bash
git remote -v
git remote add origin https://example.com/your-repo.git
```

## git push

作用：把本地提交推送到远端仓库。

示例：

```bash
git push -u origin main
```

## 简短理解

- `init`：开始使用 Git
- `add`：把改动放进待提交列表
- `commit`：正式保存一次阶段成果
- `status`：随时确认当前状态
- `log`：回看历史
- `branch`：隔离不同任务
- `remote`：连接远端仓库
- `push`：同步到远端
