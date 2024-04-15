# linux目录操作
 * ls查看当前目录文件及目录
###  cd
 * cd可进入其他目录
 * cd . . 回到上一级目录
 * cd - 回到上一次
 * cd ~ 回到当前
 * cd /   回到根目录
## pwd
 * pwd获取当前目录的绝对途径
## mkdir
 * mkdir 可以创建目录
 * mkdir -p 一次性创建多级目录
## touch
 * touch可以新建文件
## cp
  * cp复制文件到指定目录下
 * cp -r 接**目录名**     **目标目录名** 复制目录
## rm
 * rm 删除文件
 * rm -r 删除目录和目录下所有内容
## mv
 * mv 移动文件或目录
 * 重命名
## cat
 * cat 打印文件内容到屏幕
 * cat —可以带行号打印
# python操作
  ## format
  * `print('{a} {b}'.format(a,b))`
## 流程控制
- ### 条件判断
  - `input`函数类型为字符串，不能比较大小,需要用到`int`
# git的使用
## git 入门
- 先建立仓库repository
- `git init` 初始化仓库
- `git init newrepo`指定目录为git仓库
### 添加新文件
- `git add filename` 添加文件
### 提交版本
- `git commit -m "Adding files"`提交仓库
- 当我们修改了很多文件，而不想每一个都add，想commit自动来提交本地修改，我们可以使用-a标识。
`git commit -a -m "Changed some files"`
  **-a**可以将所有被修改或删除的且已经被git管理的文档提交到仓库中
### 发布版本
- `git clone ssh://example.com/~/www/project.git`
从服务器克隆一个库并上传
- `git push ssh://example.com/~/www/project.git
`修改后推送到服务器
### 取回更新
- `git pull`表示当前分支与唯一一个追踪分支合并
# github使用
## 配置git
- 创建ssh key`$ ssh-keygen -t rsa -C "your_email@youremail.com"
`
可再git bash 通过`$ ssh -T git@github.com
`确认
- 设置username 和email
  `$ git config --global user.name "your name"
$ git config --global user.email "your_email@youremail.com"
` 
- 进入要上传的仓库，右键 git bash，添加远程地址
`$ git remote add origin git@github.com:yourName/yourRepo.git
`
- 创建新文件夹，打开然后执行git init 来创建新的git仓库