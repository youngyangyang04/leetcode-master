
# 一文手把手教你搭建Git私服

## 为什么要搭建Git私服

很多同学都问文章，文档，资料怎么备份啊，自己电脑和公司电脑怎么随时同步资料啊等等，这里呢我写一个搭建自己的git私服的详细教程

为什么要搭建一个Git私服呢，而不是用Github免费的私有仓库，有以下几点：
* Github 私有仓库真的慢，文件一旦多了，或者有图片文件，git pull 的时候半天拉不下来
* 自己的文档难免有自己个人信息，放在github心里也是担心的
* 想建几个库就建几个，想几个人合作开发都可以，不香么?

**网上可以搜到很多git搭建，但是说的模棱两可**，而且有的直接是在本地搭建git服务，既然是备份，搭建在本地哪有备份的意义，一定要有一个远端服务器， 而且自己的电脑和公司的电脑还是同步自己的文章，文档和资料等等。


适合人群： 想通过git私服来备份自己的文章，Markdown，并做版本管理的同学
最后，写好每篇 Chat 是对我的责任，也是对你的尊重。谢谢大家~

正文如下：

-----------------------------

## 如何找到可以外网访问服务器

有的同学问了，自己的电脑就不能作为服务器么？

这里要说一下，安装家庭带宽，运营商默认是不会给我们独立分配公网IP的

一般情况下是一片区域公用一个公网IP池，所以外网是不能访问到在家里我们使用的电脑的

除非我们自己去做映射，这其实非常麻烦而且公网IP池 是不断变化的

辛辛苦苦做了映射，运营商给IP一换，我们的努力就白扯了

那我们如何才能找到一个外网可以访问的服务器呢，此时云计算拯救了我们。

推荐大家选一家云厂商（阿里云，腾讯云，百度云都可以）在上面上买一台云服务器

* [阿里云活动期间服务器购买](https://www.aliyun.com/minisite/goods?taskCode=shareNew2205&recordId=3641992&userCode=roof0wob)
* [腾讯云活动期间服务器购买](https://curl.qcloud.com/EiaMXllu)

云厂商经常做活动，如果从来没有买过云服务器的账号更便宜，低配一年一百块左右的样子，强烈推荐一起买个三年。

买云服务器的时候推荐直接安装centos系统。

这里要说一下，有了自己的云服务器之后 不仅仅可以用来做git私服

**同时还可以做网站，做程序后台，跑程序，做测试**（这样我们自己的电脑就不会因为自己各种搭建环境下载各种包而搞的的烂糟糟），等等等。

有自己云服务器和一个公网IP真的是一件非常非常幸福的事情，能体验到自己的服务随时可以部署上去提供给所有人使用的喜悦。

外网可以访问的服务器解决了，接下来就要部署git服务了

本文将采用centos系统来部署git私服

## 服务器端安装Git

切换至root账户

```
su root
```

看一下服务器有没有安装git，如果出现下面信息就说明是有git的
```
[root@instance-5fcyjde7 ~]# git
usage: git [--version] [--help] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   bisect     Find by binary search the change that introduced a bug
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   fetch      Download objects and refs from another repository
   grep       Print lines matching a pattern
   init       Create an empty Git repository or reinitialize an existing one
   log        Show commit logs
   merge      Join two or more development histories together
   mv         Move or rename a file, a directory, or a symlink
   pull       Fetch from and merge with another repository or a local branch
   push       Update remote refs along with associated objects
   rebase     Forward-port local commits to the updated upstream head
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   show       Show various types of objects
   status     Show the working tree status
   tag        Create, list, delete or verify a tag object signed with GPG

'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

如果没有git，就安装一下，yum安装的版本默认是 `1.8.3.1`

```
yum install git
```

安装成功之后，看一下自己安装的版本

```
git --version
```

## 服务器端设置Git账户

创建一个git的linux账户，这个账户只做git私服的操作，也是为了安全起见

如果不新创建一个linux账户，在自己的常用的linux账户下创建的话，哪天手抖 来一个`rm -rf *` 操作 数据可全没了

**这里linux git账户的密码设置的尽量复杂一些，我这里为了演示，就设置成为'gitpassword'**
```
adduser git
passwd gitpassword
```

然后就要切换成git账户，进行后面的操作了
```
[root@instance-5fcyjde7 ~]# su - git
```

看一下自己所在的目录，是不是在git目录下面

```
[git@instance-5fcyjde7 ~]$ pwd
/home/git
```

## 服务器端密钥管理

创建`.ssh` 目录，如果`.ssh` 已经存在了，可以忽略这一项

为啥用配置ssh公钥呢，同学们记不记得我急使用github上传上传代码的时候也要把自己的公钥配置上github上

这也是方面每次操作git仓库的时候不用再去输入密码

```
cd ~/
mkdir .ssh
```

进入.ssh 文件下，创建一个 `authorized_keys` 文件，这个文件就是后面就是要放我们客户端的公钥

```
cd ~/.ssh
touch authorized_keys
```

别忘了`authorized_keys`给设置权限，很多同学发现自己不能免密登陆，都是因为忘记了给`authorized_keys` 设置权限

```
chmod 700 /home/git/.ssh
chmod 600 /home/git/.ssh/authorized_keys
```

接下来我们要把客户端的公钥放在git服务器上，我们在回到客户端，创建一个公钥

在我们自己的电脑上，有公钥和私钥 两个文件分别是：`id_rsa` 和 `id_rsa.pub`

如果是`windows`系统公钥私钥的目录在`C:\Users\用户名\.ssh` 下

如果是mac 或者 linux， 公钥和私钥的目录这里 `cd ~/.ssh/`， 如果发现自己的电脑上没有公钥私钥，那就自己创建一个

创建密钥的命令

```
ssh-keygen -t rsa
```

创建密钥的过程中，一路点击回车就可以了。不需要填任何东西

把公钥拷贝到git服务器上，将我们刚刚生成的`id_rsa.pub`，拷贝到git服务器的`/home/git/.ssh/`目录

在git服务器上，将公钥添加到`authorized_keys` 文件中

```
cd /home/git/.ssh/
cat id_rsa.pub >> authorized_keys
```

如何看我们配置的密钥是否成功呢， 在客户点直接登录git服务器，看看是否是免密登陆
```
ssh git@git服务器ip
```

例如:

```
ssh git@127.0.0.1
```

如果可以免密登录，那就说明服务器端密钥配置成功了

## 服务器端部署Git 仓库

我们在登陆到git 服务器端，切换为成 git账户

如果是root账户切换成git账户
```
su - git
```

如果是其他账户切换为git账户
```
sudo su - git
```

进入git目录下
```
cd ~/git
```

创建我们的第一个Git私服的仓库，我们叫它为world仓库

那么首先创建一个文件夹名为： world.git ,然后进入这个目录

有同学问，为什么文件夹名字后面要放`.git`， 其实不这样命名也是可以的

但是细心的同学可能注意到，我们平时在github上 `git clone` 其他人的仓库的时候，仓库名字后面，都是加上`.git`的

例如下面这个例子，其实就是github对仓库名称的一个命名规则，所以我们也遵守github的命名规则。

```
git clone https://github.com/youngyangyang04/NoSQLAttack.git
```

所以我们的操作是
```
[git@localhost git]# mkdir world.git
[git@localhost git]# cd world.git
```

初始化我们的`world`仓库

```
git init --bare

```

**如果我们想创建多个仓库，就在这里创建多个文件夹并初始化就可以了，和world仓库的操作过程是一样一样的**

现在我们服务端的git仓库就部署完了，接下来就看看客户端，如何使用这个仓库呢

## 客户端连接远程仓库

我们在自己的电脑上创建一个文件夹 也叫做`world`吧

其实这里命名是随意的，但是我们为了和git服务端的仓库名称保持同步。 这样更直观我们操作的是哪一个仓库。

```
mkdir world
cd world
```

进入world文件，并初始化操作

```
cd world
git init
```

在world目录上创建一个测试文件，并且将其添加到git版本管理中

```
touch test
git add test
git commit -m "add test file"
```

将次仓库和远端仓库同步

```
git remote add origin git@git服务器端的ip:world.git
git push -u origin master
```

此时这个test测试文件就已经提交到我们的git远端私服上了

## Git私服安全问题

这里有两点安全问题

### linux git的密码不要泄露出去

否则，别人可以通过 ssh git@git服务器IP  来登陆到你的git私服服务器上

当然了，这里同学们如果买的是云厂商的云服务器的话

如果有人恶意想通过 尝试不同密码链接的方式来链接你的服务器，重试三次以上

这个客户端的IP就会被封掉，同时邮件通知我们可以IP来自哪里

所以大可放心 密码只要我们不泄露出去，基本上不会有人同时不断尝试密码的方式来登上我们的git私服服务器

### 私钥文件`id_rsa` 不要给别人

如果有人得到了这个私钥，就可以免密码登陆我们的git私服上了，我相信大家也不至于把自己的私钥主动给别人吧

## 总结

这里就是整个git私服搭建的全过程，安全问题我也给大家列举了出来，接下来好好享受自己的Git私服吧

**enjoy!**

