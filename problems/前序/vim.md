# 人生苦短，我用VIM！| 最强vim配置

> Github地址：[https://github.com/youngyangyang04/PowerVim](https://github.com/youngyangyang04/PowerVim)
> Gitee地址：[https://gitee.com/programmercarl/power-vim](https://gitee.com/programmercarl/power-vim)

熟悉我的录友，应该都知道我是vim流，无论是写代码还是写文档（Markdown），都是vim，都没用IDE。

但这里我并不是说IDE不好用，IDE在 代码跟踪，引用跳转等等其实是很给力的，效率比vim高。

我用vim的话，如果需要跟踪代码的话，就用ctag去跳转，虽然很不智能（是基于规则匹配，不是语义匹配），但加上我自己的智能就也能用（这里真的要看对代码的把握程度了）

所以连跟踪代码都不用IDE的话，其他方面那我就更用不上IDE了。

## 为什么用VIM

**至于写代码的效率，VIM完爆IDE**，其他不说，就使用IDE每次还要去碰鼠标，就很让人烦心！（真凸显了程序员的执着）

这里说一说vim的方便之处吧，搞后端开发的同学，都得玩linux吧，在linux下写代码，如果不会vim的话，会非常难受。

日常我们的开发机，线上服务器，预发布服务器，都是远端linux，需要跳板机连上去，进行操作，如果不会vim，每次都把代码拷贝到本地，修改编译，在传到远端服务器，还真的麻烦。

使用VIM的话，本地，服务器，开发机，一刀流，无缝切换，爽不。

IDE那么很吃内存，打开个IDE卡半天，用VIM就很轻便了，秒开！

而且在我们日常开发中，工作年头多了，都会发现没有纯粹的C++，Java开发啥的，就是 C++也得写，Java也得写，有时候写Go起个http服务，写Python处理一下数据，写shell搞个自动部署，编译啥的。 **总是就是啥语言就得写，一些以项目需求为导向！**

写语言还要切换不同的IDE，熟悉不同的操作规则，想想是不是很麻烦。

听说好像现在有的IDE可以支持很多语言了，这个我还不太了解，但能确定的是，IDE支持的语言再多，也不会有vim多。

**因为vim是编辑器！**，什么都可以写，不同的语言做一下相应的配置就好，写起来都是一样的顺畅。

应该不少录友感觉vim上快捷键太多了，根本记不过来，其实这和我看IDE是一样的想法，我看IDE上哪些按钮一排一排的也太多了，我都记不过来，所以索性一套vim流 扫遍所有代码，它不香么。

而且IDE集成编译、调试、智能补全、语法高亮、工程管理等等，隐藏了太多细节，使用vim，就都自己配置，想支持什么语言就自己配置，想怎么样就怎么样，需要什么就补什么，这不是很酷么？

可能有的同学感觉什么都要自己配置，有点恐惧。但一旦配置好的就非常舒服了。

**其实工程师就要逢山开路遇水搭桥，这也是最基本的素质！**

从头打在一个自己的开发利器，再舒服不过了。

## PowerVim

这里给大家介绍一下我的vim配置吧，**这套vim配置我已经打磨了将近四年**，不断调整优化，已经可以完全满足工业级打开的需求了。

所以我给它起名为PowerVim。一个真正强大的vim。

```
  _____                    __      ___
  |  __ \                   \ \    / (_)
  | |__) |____      _____ _ _\ \  / / _ _ __ ___
  |  ___/ _ \ \ /\ / / _ \ '__\ \/ / | | '_ ` _ \
  | |  | (_) \ V  V /  __/ |   \  /  | | | | | | |
  |_|   \___/ \_/\_/ \___|_|    \/   |_|_| |_| |_|
```

这个配置我开源在Github上，地址：[https://github.com/youngyangyang04/PowerVim](https://github.com/youngyangyang04/PowerVim)



来感受一下PowerVim的使用体验，看起来很酷吧！注意这些操作都不用鼠标的，一波键盘控制流！所以我平时写代码是不碰鼠标的！

![](../images/vim-01.gif)

## 安装

PowerVim的安装非常简单，我已经写好了安装脚本，只要执行以下就可以安装，而且不会影响你之前的vim配置，之前的配置都给做了备份，大家看一下脚本就知道备份在哪里了。

安装过程非常简单：
```bash
git clone https://github.com/youngyangyang04/PowerVim.git
cd PowerVim
sh install.sh
```

## 特性

目前PowerVim支持如下功能，这些都是自己配置的：

* CPP、PHP、JAVA代码补全，如果需要其他语言补全，可自行配置关键字列表在PowerVim/.vim/dictionary目录下
* 显示文件函数变量列表
* MiniBuf显示打开过的文件
* 语法高亮支持C++ (including C++11)、 Go、Java、 Php、 Html、 Json 和 Markdown
* 显示git状态，和主干或分支的添加修改删除的情况
* 显示项目文件目录，方便快速打开
* 快速注释，使用gcc注释当前行，gc注释选中的块
* 项目内搜索关键字和文件夹
* 漂亮的颜色搭配和状态栏显示

## 最后

当然 还有很多，我还详细写了PowerVim的快捷键，使用方法，插件，配置，等等，都在Github主页的README上。当时我的Github上写的都是英文README，这次为了方便大家阅读，我又翻译成中文README。

![](../images/vim-02.png)

Github地址：[https://github.com/youngyangyang04/PowerVim](https://github.com/youngyangyang04/PowerVim)

Gitee地址：[https://gitee.com/programmercarl/power-vim](https://gitee.com/programmercarl/power-vim)

最后，因为这个vim配置因为我一直没有宣传，所以star数量很少，录友们去给个star吧，真正的开发利器，值得顶起来！

