# Linux目录操作
- `ls`：查看当前目录的文件和目录
- `cd`：进入其他目录
  - `cd ..`：回到上一级目录
  - `cd -`：回到上一次的目录
  - `cd ~`：回到当前用户的主目录
  - `cd /`：回到根目录
- `pwd`：获取当前目录的绝对路径
- `mkdir`：创建目录
  - `mkdir -p`：一次性创建多级目录
- `touch`：创建文件
- `cp`：复制文件到指定目录
  - `cp -r`：复制目录到指定目录
- `rm`：删除文件
  - `rm -r`：删除目录和目录下的所有内容
- `mv`：移动文件或目录，也可用于重命名
- `cat`：打印文件内容到屏幕
  - `cat -n`：带行号打印文件内容

# Python操作
```python
print('{a} {b}'.format(a,b))  # 使用`format`函数进行字符串格式化
```

# 流程控制
- 条件判断：
  - 使用`input`函数获取输入，注意类型为字符串，需要使用`int`函数转换为整数进行比较

# Git的使用
## Git入门
- 先建立仓库（repository）
- `git init`：初始化仓库
- `git init newrepo`：指定目录为Git仓库

### 添加新文件
- `git add filename`：添加文件

### 提交版本
- `git commit -m "Adding files"`：提交仓库
- 当我们修改了很多文件，而不想每一个都`add`，想自动将所有修改提交到仓库，可以使用`-a`标识：
  `git commit -a -m "Changed some files"`
  `-a`可以将所有被修改或删除的且已经被Git管理的文档提交到仓库中

### 发布版本
```bash
git clone ssh://example.com/~/www/project.git  # 从服务器克隆一个库并上传
git push ssh://example.com/~/www/project.git   # 修改后推送到服务器
```

### 取回更新
- `git pull`：将当前分支与追踪分支合并

# GitHub使用
## 配置Git

创建SSH Key：

```shell
$ ssh-keygen -t rsa -C "your_email@youremail.com"
```

可以在Git Bash中通过以下命令来确认：

```shell
$ ssh -T git@github.com
```

设置用户名和邮箱：

```shell
$ git config --global user.name "your name"
$ git config --global user.email "your_email@youremail.com"
```

在要上传的仓库目录中，右键打开Git Bash，添加远程地址：

```shell
$ git remote add origin git@github.com:yourName/yourRepo.git
```

创建新文件夹并打开，执行`git init`来创建新的Git仓库。
