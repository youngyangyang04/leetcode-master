

# 如何在Github上提交PR（pull request）


* 如何提交代码
* 合入不规范
  * 提交信息不规范
  * Markdown 代码格式
  * pull request里的commit数量
  * 代码注释
  * 说明具体是哪种方法
  * 代码规范
  * 代码逻辑
  * 处理冲突

以下在 [https://github.com/youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master) 上提交pr为为例

## 如何合入代码

首先来说一说如何合入代码，不少录友还不太会使用github，所以这里也做一下科普。

我特意申请一个新的Github账号，给大家做一个示范。

需要强调一下，一个commit就只更新一道题目，不要很多题目一起放在一个commit里，那样就很乱。

首先LeetCode-Master每天都有更新，如何保持你fork到自己的仓库是最新的版本呢。

点击这里Fetch upstream。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20230721172815.png' width=500 alt=''></img></div>

点击之后，这里就会显示最新的信息了
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516213032568.png' width=500 alt=''></img></div>

注意这时是你的远端仓库为最新版本，本地还不是最新的，本地要git pull一下。

基于最新的版本，大家在去提交代码。

如何提交代码呢，首先把自己的代码提交到自己的fork的远端仓库中，然后open pull request，如图：

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516215102296.png' width=500 alt=''></img></div>

点击 open pull request之后，就是如下画面，一个pull request有多个commit。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516215646937.png' width=500 alt=''></img></div>

然后就是给pull request 添加备注，pull request是对本次commit的一个总结。如果一个pull request就一个commit，那么就和commit的备注保持一次。 然后点击 create pull request 就可以了

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516220219891.png' width=500 alt=''></img></div>

此时你就提交成功了，我会在项目中的pull requests 处理列表里看到你的请求。
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516220502485.png' width=500 alt=''></img></div>

然后如果你发现自己的代码没有合入多半是有问题，如果有问题都有会在pull request里给出留言的，

## 注意事项

### 提交信息不规范


大家提交代码的时候有两个地方需要写备注，一个是commit，一个是pull request，pull request包好多个commit。

commit 说清楚本文件多了哪些修改，而pull request则是对本次合入的所有commit做一个总结性描述。

commit备注，举例：添加Rust python3，那么commit备注就是：添加0001两数之和 Rust  python3 版本

而pull request 如果只有一个commit，那么就也是：添加0001两数之和 Rust  python3 版本

如果是多个commit ，则把本次commit都描述一遍。

### Markdown 语法

关于 Markdown 代码格式，例如 添加C++代码，需要有代码块语法

\`\`\`C++
C++代码
\`\`\`

例如这个commit，在添加java代码的时候，就直接添加代码
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210512141514272.png' width=500 alt=''></img></div>

正确的格式应该是这样：
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210513101029336.png' width=500 alt=''></img></div>

一般发现问题，我也会在代码中给出评论：

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/2021051309401135.png' width=500 alt=''></img></div>

这样大家也可以学习一些 提交代码的规范方面的知识


有的录友 是添加的代码块语法，但没有标记是哪种语言，这样的话 代码就不会针对某种语言高亮显示了，也比较影响阅读，例如：

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/2021051214212374.png' width=500 alt=''></img></div>

提交python代码的话，要注释好，是python2还是python3

例如这样：

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210513174147165.png' width=500 alt=''></img></div>

当然python2的话，只这么写就行

\`\`\`python
python代码
\`\`\`

### pull request里的commit数量


有的录友是一个pull request 里有很多commit （一个commit是一道题目的代码）。

有的录友是一个pull request 里只有一个commit。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210512221535670.png' width=500 alt=''></img></div>

其实如果大家是平时一天写了两三道题目的话，那么分三个commit，一个pull request提交上来就行。

一个pull request 一个commit也可以，这样大家就会麻烦一点。

但注意一个pull request也不要放太多的commit，一旦有一道题目代码不合格，我没有合入，就这个pull request里影响其他所有代码的合入了。

### 代码注释

提交的代码最好要有注释，这样也方便读者理解。

例如这位录友，在提交Java代码的时候，按照题解的意思对Java版本的代码进行的注释，这就很棒👍

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210512212151438.png' width=500 alt=''></img></div>

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210513101321112.png' width=500 alt=''></img></div>

当然如果大家感觉 已有的代码 不符合以上要求的话，例如 代码思路不够清晰不够规范，注释不够友好，依然欢迎提交优化代码，要记得详细注释哦。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210516082342756.png' width=500 alt=''></img></div>

### 说明具体是哪种方法

有的题解有两种甚至三四种解法，在添加代码的时候，注释上也清楚具体是哪一种方法的版本。

下面这位录友做的就很好

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210512221951251.png' width=500 alt=''></img></div>


<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210513101551819.png' width=500 alt=''></img></div>

有的题解，是一起给出了多道题目的讲解，例如项目中0102.二叉树的层序遍历.md 中有八道题目，那么大家添加代码的时候 应该在代码注释上，或者 直接写上 是哪个题目的代码。


### 代码规范


大家提交代码要规范，当然代码可以在力扣上运行通过是最基本的。

虽然我主张没有绝对正确的代码风格，但既然是给LeetCode-Master提交代码，尽量遵循Google编程规范。

经常看我的代码的录友应该都知道，我的代码风格严格按照 Google C++ 编程规范来的，这样看上去会比较整洁。

大家提交代码的时候遇到规范性问题，例如哪里应该有空格，哪里没有空格，可以参考我的代码来。

有一位录友在提交代码的时候会把之前的代码 做一下规范性的调整，这就很棒。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210514093012603.png' width=500 alt=''></img></div>

**代码规范从你我做起！**


### 代码逻辑

**提交的代码要按照题解思路来写**。

虽然大家自己发挥想象空间是好的，但是题解还是要一脉相承，读者看完题解，发现代码和题解不是一个思路的话，那和重新读代码有啥区别了。

所以和题解不是一个思路的代码，除非详细注释了自己的思路 或者 写一段自己代码的描述说明思路和优化的地方，否则我就不会通过合入了哈。

大家的代码 最好也将关键地方放上注释，这样有助于别人快速理解你的代码。


### 处理冲突

在合入的过程中还要处理冲突的代码， 理解大家代码的思路，解决冲突，然后在力扣提交一下，确保是没问题。

例如同一道题目， 一位录友提交了， 我还没处理如何，另一位录友也对这道题也提交了代码，这样就会发生冲突
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210514092248192.png' width=500 alt=''></img></div>

大家提交代码的热情太高了，我有时候根本处理不过来，但我必须当天处理完，否则第二天代码冲突会越来越多。
<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210514091457392.png' width=500 alt=''></img></div>

一天晚上分别有两位录友提交了 30多道 java代码，全部冲突，解决冲突处理的我脖子疼[哭]

那么在处理冲突的时候 保留谁的代码，删点谁的代码呢？

我一定是看谁 代码逻辑和题解一致，代码风格好，注释友好，就保留谁的。

所以例如当你想提交Java代码的时候，即使发现该题解已经有Java版本了，只要你的代码写的好，一样可以提交，我评审合格一样可以合入代码库。


### 不要做额外修改

确保这种额外文件不要提交。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210514093430534.png' width=500 alt=''></img></div>

还有添加不同方法的时候，直接用正文格式写，哪种方法就可以了，不要添加目录 ，例如这样，这样整篇文章目录结构就有影响了。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210513102640556.png' width=500 alt=''></img></div>

前面不要加 `## 前序遍历（迭代法）`，直接写`前序遍历（迭代法）`就可以了。

当然这里也没有给代码块标记上对应的语言，应该是

\`\`\` Go
Go语言代码
\`\`\`


## 对代码保持敬畏

有的录友甚至提交的代码并不是本题的代码，虽然我是鼓励大家提交代码的，但是大家贡献代码的时候也要对 自己的代码有敬畏之心，自己的代码是要给很多读者看的。

* 代码运行无误
* 写的够不够简洁
* 注释清不清晰
* 备注规不规范

这也是培养大家以后协调工作的一种能力。

## 优化

目前 leetcode-master中大部分题解已经补充了其他语言，但如果你发现了可以优化的地方，依然可以提交PR来优化。

甚至发现哪里有语病，也欢迎提交PR来修改，例如下面：就是把【下表】 纠正为【下标】

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210811144337.png' width=500 alt=''></img></div>

不用非要写出牛逼的代码才能提交PR，只要发现 文章中有任何问题，或者错别字，都欢迎提交PR，成为contributor。

<div align="center"><img src='https://code-thinking-1253855093.file.myqcloud.com/pics/20210927113149.png' width=500 alt=''></img></div>

## 特别注意

git add之前，要git diff 查看一下，本次提交所修改的代码是不是 自己修改的，是否 误删，或者误加的文件。

提交代码，不要使用git push -f 这种命令，要足够了解 -f 意味着什么。



