## 一些闲话：

> 1. **介绍**：本项目是一套完整的刷题计划，旨在帮助大家少走弯路，循序渐进学算法，[关注作者](#关于作者)
> 2. **PDF版本** ： [「代码随想录」算法精讲 PDF 版本](https://mp.weixin.qq.com/s/RsdcQ9umo09R6cfnwXZlrQ) 。
> 3. **知识星球** : 面试技巧/如何选择offer/大厂内推/职场规则/简历修改/技术分享/程序人生。欢迎加入[我的知识星球](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ) 。
> 4. **转载须知** ：以下所有文章皆为我（[程序员Carl](https://github.com/youngyangyang04)）的原创。引用本项目文章请注明出处，发现恶意抄袭或搬运，会动用法律武器维护自己的权益。让我们一起维护一个良好的技术创作环境！

<p align="center">
<a href="https://github.com/youngyangyang04/leetcode-master" target="_blank">
	<img src="https://img-blog.csdnimg.cn/20210318112734278.png" width="300"/>
</a>

<p align="center">
  <a href="https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ"><img src="https://img.shields.io/badge/知识星球-代码随想录-blue" alt=""></a>
  <a href="https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw"><img src="https://img.shields.io/badge/刷题-微信群-green" alt=""></a>
  <a href="https://img-blog.csdnimg.cn/20201210231711160.png"><img src="https://img.shields.io/badge/公众号-代码随想录-brightgreen" alt=""></a>
  <a href="https://space.bilibili.com/525438321"><img src="https://img.shields.io/badge/B站-代码随想录-orange" alt=""></a>
</p>

# LeetCode 刷题攻略

## 刷题攻略的背景

很多刚开始刷题的同学都有一个困惑：面对leetcode上近两千道题目，从何刷起。

其实我之前在知乎上回答过这个问题，回答内容大概是按照如下类型来刷数组-> 链表-> 哈希表->字符串->栈与队列->树->回溯->贪心->动态规划->图论->高级数据结构，再从简单刷起，做了几个类型题目之后，再慢慢做中等题目、困难题目。

但我能设身处地的感受到：即使有这样一个整体规划，对于一位初学者甚至算法老手寻找合适自己的题目也是很困难，时间成本很高，而且题目还不一定就是经典题目。

对于刷题，我们都是想用最短的时间把经典题目都做一篇，这样效率才是最高的！

所以我整理了leetcode刷题攻略：一个超级详细的刷题顺序，**每道题目都是我精心筛选，都是经典题目高频面试题**，大家只要按照这个顺序刷就可以了，**你没看错，就是题目顺序都排好了，文章顺序就是刷题顺序！挨个刷就可以，不用自己再去题海里选题了！**

而且每道题目我都写了的详细题解（图文并茂，难点配有视频），力扣上我的题解都是排在对应题目的首页，质量是有目共睹的。

**那么今天我把这个刷题顺序整理出来，是为了帮助更多的学习算法的同学少走弯路！**

如果你在刷leetcode，强烈建议先按照本攻略刷题顺序来刷，刷完了你会发现对整个知识体系有一个质的飞跃，不用在题海茫然的寻找方向。

**文章会首发在公众号[「代码随想录」](https://img-blog.csdnimg.cn/20201124161234338.png)，赶紧去看看吧，你一定会发现相见恨晚！**

## 如何使用该刷题攻略

电脑端还看不到留言，大家可以在公众号[「代码随想录」](https://img-blog.csdnimg.cn/20201124161234338.png)，左下角有「算法汇总」，这是手机版刷题攻略，看完就会发现有很多录友（代码随想录的朋友们）在文章下留言打卡，这份刷题顺序和题解已经陪伴了上万录友了，同时也说明文章的质量是经过上万人的考验！

欢迎每一位学习算法的小伙伴加入到这个学习阵营来！

**目前已经更新了，数组-> 链表-> 哈希表->字符串->栈与队列->树->回溯->贪心，八个专题了，正在讲解动态规划！**

在刷题指南中，每个专题开始都有理论基础篇，并不像是教科书般的理论介绍，而是从实战中归纳需要的基础知识。每个专题结束都有总结篇，最这个专题的归纳总结。

如果你是算法老手，这篇攻略也是复习的最佳资料，如果把每个系列对应的总结篇，快速过一遍，整个算法知识体系以及各种解法就重现脑海了。

在按照如下顺序刷题的过程中，每一道题解一定要看对应文章下面的留言（留言目前只能在手机端查看）。

如果你有疑问或者发现文章哪里有不对的地方，都可以在留言区都能找到答案，还有很多录友的总结非常赞，看完之后也很有收获。

目前「代码随想录」刷题指南更新了：**200篇文章，精讲了100多道经典算法题目，共50w字的详细图解，部分难点题目还搭配了20分钟左右的视频讲解**。

准备好了么，刷题攻略开始咯，go go go！

---------------------------------------------

## 前序

* [代码随想录后序安排](https://mp.weixin.qq.com/s/4eeGJREy6E-v6D7cR_5A4g)
* [代码随想录知识星球](https://mp.weixin.qq.com/s/X1XCH-KevURi3LnakJsCkA)

* 编程语言
    * [C++面试&C++学习指南知识点整理](https://github.com/youngyangyang04/TechCPP)

* 编程素养
    * [看了这么多代码，谈一谈代码风格！](./problems/前序/代码风格.md.md)
    * [力扣上的代码想在本地编译运行？](./problems/前序/力扣上的代码想在本地编译运行？.md)
    * [什么是核心代码模式，什么又是ACM模式？](./problems/前序/什么是核心代码模式，什么又是ACM模式？.md)
* 工具 
    * [一站式vim配置](https://github.com/youngyangyang04/PowerVim)
    * [保姆级Git入门教程，万字详解](https://mp.weixin.qq.com/s/Q_O0ey4C9tryPZaZeJocbA)
    * [程序员应该用什么用具来写文档？](./problems/前序/程序员写文档工具.md)

* 求职 
    * [程序员的简历应该这么写！！（附简历模板）](./problems/前序/程序员简历.md)
    * [BAT级别技术面试流程和注意事项都在这里了](./problems/前序/BAT级别技术面试流程和注意事项都在这里了.md)
    * [北京有这些互联网公司，你都知道么？](./problems/前序/北京互联网公司总结.md)
    * [上海有这些互联网公司，你都知道么？](./problems/前序/上海互联网公司总结.md)
    * [深圳有这些互联网公司，你都知道么？](./problems/前序/深圳互联网公司总结.md)
    * [广州有这些互联网公司，你都知道么？](./problems/前序/广州互联网公司总结.md)
    * [成都有这些互联网公司，你都知道么？](./problems/前序/成都互联网公司总结.md)
    * [杭州有这些互联网公司，你都知道么？](./problems/前序/杭州互联网公司总结.md)
    
* 算法性能分析
    * [关于时间复杂度，你不知道的都在这里！](./problems/前序/关于时间复杂度，你不知道的都在这里！.md)
    * [O(n)的算法居然超时了，此时的n究竟是多大？](./problems/前序/On的算法居然超时了，此时的n究竟是多大？.md)
    * [通过一道面试题目，讲一讲递归算法的时间复杂度！](./problems/前序/通过一道面试题目，讲一讲递归算法的时间复杂度！.md)
    * [本周小结！（算法性能分析系列一）](./problems/周总结/20201210复杂度分析周末总结.md)
    * [关于空间复杂度，可能有几个疑问？](./problems/前序/关于空间复杂度，可能有几个疑问？.md)
    * [递归算法的时间与空间复杂度分析！](./problems/前序/递归算法的时间与空间复杂度分析.md)
    * [刷了这么多题，你了解自己代码的内存消耗么？](./problems/前序/刷了这么多题，你了解自己代码的内存消耗么？.md)

（持续更新中.....）

## 数组 

1. [数组过于简单，但你该了解这些！](./problems/数组理论基础.md) 
2. [数组：每次遇到二分法，都是一看就会，一写就废](./problems/0704.二分查找.md)
3. [数组：就移除个元素很难么？](./problems/0027.移除元素.md)
4. [数组：滑动窗口拯救了你](./problems/0209.长度最小的子数组.md)
5. [数组：这个循环可以转懵很多人！](./problems/0059.螺旋矩阵II.md)
6. [数组：总结篇](./problems/数组总结篇.md)

## 链表

1. [关于链表，你该了解这些！](./problems/链表理论基础.md)
2. [链表：听说用虚拟头节点会方便很多？](./problems/0203.移除链表元素.md)
3. [链表：一道题目考察了常见的五个操作！](./problems/0707.设计链表.md)
4. [链表：听说过两天反转链表又写不出来了？](./problems/0206.翻转链表.md)
5. [链表：删除链表的倒数第 N 个结点](./problems/0019.删除链表的倒数第N个节点.md)
5. [链表：环找到了，那入口呢？](./problems/0142.环形链表II.md)
6. [链表：总结篇！](./problems/链表总结篇.md)

## 哈希表

1. [关于哈希表，你该了解这些！](./problems/哈希表理论基础.md)
2. [哈希表：可以拿数组当哈希表来用，但哈希值不要太大](./problems/0242.有效的字母异位词.md)
3. [哈希表：哈希值太大了，还是得用set](./problems/0349.两个数组的交集.md)
4. [哈希表：用set来判断快乐数](./problems/0202.快乐数.md)
5. [哈希表：map等候多时了](./problems/0001.两数之和.md)
6. [哈希表：其实需要哈希的地方都能找到map的身影](./problems/0454.四数相加II.md)
7. [哈希表：这道题目我做过？](./problems/0383.赎金信.md)
8. [哈希表：解决了两数之和，那么能解决三数之和么？](./problems/0015.三数之和.md)
9. [双指针法：一样的道理，能解决四数之和](./problems/0018.四数之和.md)
10. [哈希表：总结篇！（每逢总结必经典）](./problems/哈希表总结.md)


## 字符串

1. [字符串：这道题目，使用库函数一行代码搞定](./problems/0344.反转字符串.md)
2. [字符串：简单的反转还不够！](./problems/0541.反转字符串II.md)
3. [字符串：替换空格](./problems/剑指Offer05.替换空格.md)
4. [字符串：花式反转还不够！](./problems/0151.翻转字符串里的单词.md)
5. [字符串：反转个字符串还有这个用处？](./problems/剑指Offer58-II.左旋转字符串.md)
6. [帮你把KMP算法学个通透](./problems/0028.实现strStr.md)
8. [字符串：KMP算法还能干这个！](./problems/0459.重复的子字符串.md)
9. [字符串：总结篇！](./problems/字符串总结.md)

## 双指针法 

双指针法基本都是应用在数组，字符串与链表的题目上

1. [数组：就移除个元素很难么？](./problems/0027.移除元素.md)
2. [字符串：这道题目，使用库函数一行代码搞定](./problems/0344.反转字符串.md)
3. [字符串：替换空格](./problems/剑指Offer05.替换空格.md)
4. [字符串：花式反转还不够！](./problems/0151.翻转字符串里的单词.md)
5. [链表：听说过两天反转链表又写不出来了？](./problems/0206.翻转链表.md)
6. [链表：环找到了，那入口呢？](./problems/0142.环形链表II.md)
7. [哈希表：解决了两数之和，那么能解决三数之和么？](./problems/0015.三数之和.md)
8. [双指针法：一样的道理，能解决四数之和](./problems/0018.四数之和.md)
9. [双指针法：总结篇！](./problems/双指针总结.md)

## 栈与队列

1. [栈与队列：来看看栈和队列不为人知的一面](./problems/栈与队列理论基础.md)
2. [栈与队列：我用栈来实现队列怎么样？](./problems/0232.用栈实现队列.md)
3. [栈与队列：用队列实现栈还有点别扭](./problems/0225.用队列实现栈.md)
4. [栈与队列：系统中处处都是栈的应用](./problems/0020.有效的括号.md)
5. [栈与队列：匹配问题都是栈的强项](./problems/1047.删除字符串中的所有相邻重复项.md)
6. [栈与队列：有没有想过计算机是如何处理表达式的？](./problems/0150.逆波兰表达式求值.md)
7. [栈与队列：滑动窗口里求最大值引出一个重要数据结构](./problems/0239.滑动窗口最大值.md)
8. [栈与队列：求前 K 个高频元素和队列有啥关系？](./problems/0347.前K个高频元素.md)
9. [栈与队列：总结篇！](./problems/栈与队列总结.md)

## 二叉树 

题目分类大纲如下：           
<img src='https://img-blog.csdnimg.cn/20210219190809451.png' width=600 alt='二叉树大纲'> </img></div>

1. [关于二叉树，你该了解这些！](./problems/二叉树理论基础.md)
2. [二叉树：一入递归深似海，从此offer是路人](./problems/二叉树的递归遍历.md)
3. [二叉树：听说递归能做的，栈也能做！](./problems/二叉树的迭代遍历.md)
4. [二叉树：前中后序迭代方式的写法就不能统一一下么？](./problems/二叉树的统一迭代法.md)
5. [二叉树：层序遍历登场！](./problems/0102.二叉树的层序遍历.md) 
6. [二叉树：你真的会翻转二叉树么？](./problems/0226.翻转二叉树.md)
7. [本周小结！（二叉树）](./problems/周总结/20200927二叉树周末总结.md)
8. [二叉树：我对称么？](./problems/0101.对称二叉树.md)
9. [二叉树：看看这些树的最大深度](./problems/0104.二叉树的最大深度.md)
10. [二叉树：看看这些树的最小深度](./problems/0111.二叉树的最小深度.md)
11. [二叉树：我有多少个节点？](./problems/0222.完全二叉树的节点个数.md)
12. [二叉树：我平衡么？](./problems/0110.平衡二叉树.md)
13. [二叉树：找我的所有路径？](./problems/0257.二叉树的所有路径.md)
14. [本周总结！二叉树系列二](./problems/周总结/20201003二叉树周末总结.md)
15. [二叉树：以为使用了递归，其实还隐藏着回溯](./problems/二叉树中递归带着回溯.md)
16. [二叉树：做了这么多题目了，我的左叶子之和是多少？](./problems/0404.左叶子之和.md)
17. [二叉树：我的左下角的值是多少？](./problems/0513.找树左下角的值.md)
18. [二叉树：递归函数究竟什么时候需要返回值，什么时候不要返回值？](./problems/0112.路径总和.md)
19. [二叉树：构造二叉树登场！](./problems/0106.从中序与后序遍历序列构造二叉树.md)
20. [二叉树：构造一棵最大的二叉树](./problems/0654.最大二叉树.md)
21. [本周小结！（二叉树系列三）](./problems/周总结/20201010二叉树周末总结.md) 
22. [二叉树：合并两个二叉树](./problems/0617.合并二叉树.md)
23. [二叉树：二叉搜索树登场！](./problems/0700.二叉搜索树中的搜索.md)
24. [二叉树：我是不是一棵二叉搜索树](./problems/0098.验证二叉搜索树.md)
25. [二叉树：搜索树的最小绝对差](./problems/0530.二叉搜索树的最小绝对差.md)
26. [二叉树：我的众数是多少？](./problems/0501.二叉搜索树中的众数.md)
27. [二叉树：公共祖先问题](./problems/0236.二叉树的最近公共祖先.md)
28. [本周小结！（二叉树系列四）](./problems/周总结/20201017二叉树周末总结.md)
29. [二叉树：搜索树的公共祖先问题](./problems/0235.二叉搜索树的最近公共祖先.md)
30. [二叉树：搜索树中的插入操作](./problems/0701.二叉搜索树中的插入操作.md)
31. [二叉树：搜索树中的删除操作](./problems/0450.删除二叉搜索树中的节点.md)
32. [二叉树：修剪一棵搜索树](./problems/0669.修剪二叉搜索树.md)
33. [二叉树：构造一棵搜索树](./problems/0108.将有序数组转换为二叉搜索树.md)
34. [二叉树：搜索树转成累加树](./problems/0538.把二叉搜索树转换为累加树.md)
35. [二叉树：总结篇！（需要掌握的二叉树技能都在这里了）](./problems/二叉树总结篇.md)
 
## 回溯算法 

题目分类大纲如下：             

<img src='https://img-blog.csdnimg.cn/20210219192050666.png' width=600 alt='回溯算法大纲'> </img></div>

1. [关于回溯算法，你该了解这些！](./problems/回溯算法理论基础.md)
2. [回溯算法：组合问题](./problems/0077.组合.md)
3. [回溯算法：组合问题再剪剪枝](./problems/0077.组合优化.md)
4. [回溯算法：求组合总和！](./problems/0216.组合总和III.md)
5. [回溯算法：电话号码的字母组合](./problems/0017.电话号码的字母组合.md)
6. [本周小结！（回溯算法系列一）](./problems/周总结/20201030回溯周末总结.md)
7. [回溯算法：求组合总和（二）](./problems/0039.组合总和.md)
8. [回溯算法：求组合总和（三）](./problems/0040.组合总和II.md)
9. [回溯算法：分割回文串](./problems/0131.分割回文串.md)
10. [回溯算法：复原IP地址](./problems/0093.复原IP地址.md)
11. [回溯算法：求子集问题！](./problems/0078.子集.md)
12. [本周小结！（回溯算法系列二）](./problems/周总结/20201107回溯周末总结.md)
13. [回溯算法：求子集问题（二）](./problems/0090.子集II.md)
14. [回溯算法：递增子序列](./problems/0491.递增子序列.md)
15. [回溯算法：排列问题！](./problems/0046.全排列.md)
16. [回溯算法：排列问题（二）](./problems/0047.全排列II.md)
17. [本周小结！（回溯算法系列三）](./problems/周总结/20201112回溯周末总结.md)
18. [回溯算法去重问题的另一种写法](./problems/回溯算法去重问题的另一种写法.md)

23. [回溯算法：重新安排行程](./problems/0332.重新安排行程.md)
24. [回溯算法：N皇后问题](./problems/0051.N皇后.md)
25. [回溯算法：解数独](./problems/0037.解数独.md)
26. [一篇总结带你彻底搞透回溯算法！](./problems/回溯总结.md)

## 贪心算法 

题目分类大纲如下：             

<img src='https://img-blog.csdnimg.cn/20210220152245584.png' width=600 alt='贪心算法大纲'> </img></div>

1. [关于贪心算法，你该了解这些！](https://mp.weixin.qq.com/s/O935TaoHE9Eexwe_vSbRAg)
2. [贪心算法：分发饼干](https://mp.weixin.qq.com/s/YSuLIAYyRGlyxbp9BNC1uw)
3. [贪心算法：摆动序列](https://mp.weixin.qq.com/s/Xytl05kX8LZZ1iWWqjMoHA)
4. [贪心算法：最大子序和](https://mp.weixin.qq.com/s/DrjIQy6ouKbpletQr0g1Fg)
5. [本周小结！（贪心算法系列一）](https://mp.weixin.qq.com/s/KQ2caT9GoVXgB1t2ExPncQ)
6. [贪心算法：买卖股票的最佳时机II](https://mp.weixin.qq.com/s/VsTFA6U96l18Wntjcg3fcg)
7. [贪心算法：跳跃游戏](https://mp.weixin.qq.com/s/606_N9j8ACKCODoCbV1lSA)
8. [贪心算法：跳跃游戏II](https://mp.weixin.qq.com/s/kJBcsJ46DKCSjT19pxrNYg)
9. [贪心算法：K次取反后最大化的数组和](https://mp.weixin.qq.com/s/dMTzBBVllRm_Z0aaWvYazA)
10. [本周小结！（贪心算法系列二）](https://mp.weixin.qq.com/s/RiQri-4rP9abFmq_mlXNiQ)
11. [贪心算法：加油站](https://mp.weixin.qq.com/s/aDbiNuEZIhy6YKgQXvKELw)
12. [贪心算法：分发糖果](https://mp.weixin.qq.com/s/8MwlgFfvaNYmjGwjuMlETQ)
13. [贪心算法：柠檬水找零](https://mp.weixin.qq.com/s/0kT4P-hzY7H6Ae0kjQqnZg)
14. [贪心算法：根据身高重建队列](https://mp.weixin.qq.com/s/-2TgZVdOwS-DvtbjjDEbfw)
15. [本周小结！（贪心算法系列三）](https://mp.weixin.qq.com/s/JfeuK6KgmifscXdpEyIm-g)
16. [贪心算法：根据身高重建队列（续集）](https://mp.weixin.qq.com/s/K-pRN0lzR-iZhoi-1FgbSQ)
17. [贪心算法：用最少数量的箭引爆气球](https://mp.weixin.qq.com/s/HxVAJ6INMfNKiGwI88-RFw)
18. [贪心算法：无重叠区间](https://mp.weixin.qq.com/s/oFOEoW-13Bm4mik-aqAOmw)
19. [贪心算法：划分字母区间](https://mp.weixin.qq.com/s/pdX4JwV1AOpc_m90EcO2Hw)
20. [贪心算法：合并区间](https://mp.weixin.qq.com/s/royhzEM5tOkUFwUGrNStpw)
21. [本周小结！（贪心算法系列四）](https://mp.weixin.qq.com/s/zAMHT6JfB19ZSJNP713CAQ)
22. [贪心算法：单调递增的数字](https://mp.weixin.qq.com/s/TAKO9qPYiv6KdMlqNq_ncg)
23. [贪心算法：买卖股票的最佳时机含手续费](https://mp.weixin.qq.com/s/olWrUuDEYw2Jx5rMeG7XAg)
24. [贪心算法：我要监控二叉树！](https://mp.weixin.qq.com/s/kCxlLLjWKaE6nifHC3UL2Q)
25. [贪心算法：总结篇！（每逢总结必经典）](https://mp.weixin.qq.com/s/ItyoYNr0moGEYeRtcjZL3Q)

## 动态规划

动态规划专题已经开始啦，来不及解释了，小伙伴们上车别掉队！

1. [关于动态规划，你该了解这些！](https://mp.weixin.qq.com/s/ocZwfPlCWrJtVGACqFNAag)
2. [动态规划：斐波那契数](https://mp.weixin.qq.com/s/ko0zLJplF7n_4TysnPOa_w)
3. [动态规划：爬楼梯](https://mp.weixin.qq.com/s/Ohop0jApSII9xxOMiFhGIw)
4. [动态规划：使用最小花费爬楼梯](https://mp.weixin.qq.com/s/djZB9gkyLFAKcQcSvKDorA)
5. [本周小结！（动态规划系列一）](https://mp.weixin.qq.com/s/95VqGEDhtBBBSb-rM4QSMA)
6. [动态规划：不同路径](https://mp.weixin.qq.com/s/MGgGIt4QCpFMROE9X9he_A)
7. [动态规划：不同路径还不够，要有障碍！](https://mp.weixin.qq.com/s/lhqF0O4le9-wvalptOVOww)
8. [动态规划：整数拆分，你要怎么拆？](https://mp.weixin.qq.com/s/cVbyHrsWH_Rfzlj-ESr01A)
9. [动态规划：不同的二叉搜索树](https://mp.weixin.qq.com/s/8VE8pDrGxTf8NEVYBDwONw)
10. [本周小结！（动态规划系列二）](https://mp.weixin.qq.com/s/VVsDwTP57g1f9aVsg6wShw)

背包问题系列：

<img src='https://img-blog.csdnimg.cn/202102261550480.png' width=500 alt='背包问题大纲'> </img></div>

11. [动态规划：关于01背包问题，你该了解这些！](https://mp.weixin.qq.com/s/FwIiPPmR18_AJO5eiidT6w)
12. [动态规划：关于01背包问题，你该了解这些！（滚动数组）](https://mp.weixin.qq.com/s/M4uHxNVKRKm5HPjkNZBnFA)
13. [动态规划：分割等和子集可以用01背包！](https://mp.weixin.qq.com/s/sYw3QtPPQ5HMZCJcT4EaLQ)
14. [动态规划：最后一块石头的重量 II](https://mp.weixin.qq.com/s/WbwAo3jaUaNJjvhHgq0BGg)
15. [本周小结！（动态规划系列三）](https://mp.weixin.qq.com/s/7emRqR1O3scH63jbaE678A)
16. [动态规划：目标和！](https://mp.weixin.qq.com/s/2pWmaohX75gwxvBENS-NCw)
17. [动态规划：一和零！](https://mp.weixin.qq.com/s/x-u3Dsp76DlYqtCe0xEKJw) 
18. [动态规划：关于完全背包，你该了解这些！](https://mp.weixin.qq.com/s/akwyxlJ4TLvKcw26KB9uJw)
19. [动态规划：给你一些零钱，你要怎么凑？](https://mp.weixin.qq.com/s/PlowDsI4WMBOzf3q80AksQ)
20. [本周小结！（动态规划系列四）](https://mp.weixin.qq.com/s/vfEXwcOlrSBBcv9gg8VDJQ)
21. [动态规划：Carl称它为排列总和！](https://mp.weixin.qq.com/s/Iixw0nahJWQgbqVNk8k6gA)
22. [动态规划：以前我没得选，现在我选择再爬一次！](https://mp.weixin.qq.com/s/e_wacnELo-2PG76EjrUakA)
23. [动态规划： 给我个机会，我再兑换一次零钱](https://mp.weixin.qq.com/s/dyk-xNilHzNtVdPPLObSeQ)
24. [动态规划：一样的套路，再求一次完全平方数](https://mp.weixin.qq.com/s/VfJT78p7UGpDZsapKF_QJQ)
25. [本周小结！（动态规划系列五）](https://mp.weixin.qq.com/s/znj-9j8mWymRFaPjJN2Qnw)
26. [动态规划：单词拆分](https://mp.weixin.qq.com/s/3Spx1B6MbIYjS8YkVbByzA)
27. [动态规划：关于多重背包，你该了解这些！](https://mp.weixin.qq.com/s/b-UUUmbvG7URWyCjQkiuuQ)
28. [听说背包问题很难？ 这篇总结篇来拯救你了](https://mp.weixin.qq.com/s/ZOehl3U1mDiyOQjFG1wNJA)

打家劫舍系列：

29. [动态规划：开始打家劫舍！](https://mp.weixin.qq.com/s/UZ31WdLEEFmBegdgLkJ8Dw)
30. [动态规划：继续打家劫舍！](https://mp.weixin.qq.com/s/kKPx4HpH3RArbRcxAVHbeQ)
31. [动态规划：还要打家劫舍！](https://mp.weixin.qq.com/s/BOJ1lHsxbQxUZffXlgglEQ)

股票系列：

<img src='https://code-thinking.cdn.bcebos.com/pics/%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98%E6%80%BB%E7%BB%93.jpg' width=500 alt='股票问题总结'> </img></div>

32. [动态规划：买卖股票的最佳时机](https://mp.weixin.qq.com/s/keWo5qYJY4zmHn3amfXdfQ)
33. [动态规划：本周我们都讲了这些（系列六）](https://mp.weixin.qq.com/s/GVu-6eF0iNkpVDKRXTPOTA)
33. [动态规划：买卖股票的最佳时机II](https://mp.weixin.qq.com/s/d4TRWFuhaY83HPa6t5ZL-w)
34. [动态规划：买卖股票的最佳时机III](https://mp.weixin.qq.com/s/Sbs157mlVDtAR0gbLpdKzg)
35. [动态规划：买卖股票的最佳时机IV](https://mp.weixin.qq.com/s/jtxZJWAo2y5sUsW647Z5cw)
36. [动态规划：最佳买卖股票时机含冷冻期](https://mp.weixin.qq.com/s/TczJGFAPnkjH9ET8kwH1OA)
37. [动态规划：本周我们都讲了这些（系列七）](https://mp.weixin.qq.com/s/vdzDlrEvhXWRzblTnOnzKg)
38. [动态规划：买卖股票的最佳时机含手续费](https://mp.weixin.qq.com/s/2Cd_uINjerZ25VHH0K2IBQ)
39. [动态规划：股票系列总结篇](https://mp.weixin.qq.com/s/sC5XyEtDQWkonKnbCvZhDw)

子序列系列： 

40. [动态规划：最长递增子序列](https://mp.weixin.qq.com/s/f8nLO3JGfgriXep_gJQpqQ)
41. [动态规划：最长连续递增序列](https://mp.weixin.qq.com/s/c0Nn0TtjkTISVdqRsyMmyA)
42. [动态规划：最长重复子数组](https://mp.weixin.qq.com/s/U5WaWqBwdoxzQDotOdWqZg)
43. [动态规划：最长公共子序列](https://mp.weixin.qq.com/s/Qq0q4HaE4TyasCTj2WGFOg)
44. [动态规划：本周我们都讲了这些（系列八）](https://mp.weixin.qq.com/s/KJNNOzGxTYhr1ks7tHvk0g)
45. [动态规划：不相交的线](https://mp.weixin.qq.com/s/krfYzSYEO8jIoVfyHzR0rw)
46. [动态规划：最大子序和](https://mp.weixin.qq.com/s/2Xtyi2L4r8sM-BcxgUKmcA)
47. [动态规划：判断子序列](https://mp.weixin.qq.com/s/2pjT4B4fjfOx5iB6N6xyng)
48. [动态规划：不同的子序列](https://mp.weixin.qq.com/s/1SULY2XVSROtk_hsoVLu8A)
49. [动态规划：两个字符串的删除操作](https://mp.weixin.qq.com/s/a8BerpqSf76DCqkPDJrpYg)
50. [动态规划：本周我们都讲了这些（系列十）](https://mp.weixin.qq.com/s/ES1SXf54047496YnNdeirA)
51. [动态规划：编辑距离](https://mp.weixin.qq.com/s/8aG71XjSgZG6kZbiAdkJnQ)
52. [为了绝杀编辑距离，我做了三步铺垫，你都知道么？](https://mp.weixin.qq.com/s/kbs4kCUzg8gPFttF9H3Yyw)
53. [动态规划：回文子串](https://mp.weixin.qq.com/s/2WetyP6IYQ6VotegepVpEw)
54. [动态规划：最长回文子序列](https://mp.weixin.qq.com/s/jbd3p4QPm5Kh1s2smTzWag)


（持续更新中....）

## 图论 

## 十大排序

## 数论 

## 高级数据结构经典题目 

* 并查集 
* 最小生成树 
* 线段树 
* 树状数组 
* 字典树 

## 海量数据处理

# 算法模板 

[各类基础算法模板](https://github.com/youngyangyang04/leetcode/blob/master/problems/算法模板.md)

# 知识星球精选

1. [选择方向的时候，我也迷茫了](https://mp.weixin.qq.com/s/ZCzFiAHZHLqHPLJQXNm75g)
2. [刷题就用库函数了，怎么了？](https://mp.weixin.qq.com/s/6K3_OSaudnHGq2Ey8vqYfg)

# B站算法视频讲解 

以下为[B站「代码随想录」](https://space.bilibili.com/525438321)算法讲解视频：

* [帮你把KMP算法学个通透！（理论篇）](https://www.bilibili.com/video/BV1PD4y1o7nd)
* [帮你把KMP算法学个通透！（代码篇）](https://www.bilibili.com/video/BV1M5411j7Xx)
* [带你学透回溯算法（理论篇）](https://www.bilibili.com/video/BV1cy4y167mM)
* [回溯算法之组合问题（力扣题目：77.组合）](https://www.bilibili.com/video/BV1ti4y1L7cv)
* [组合问题的剪枝操作（对应力扣题目：77.组合）](https://www.bilibili.com/video/BV1wi4y157er)
* [组合总和（对应力扣题目：39.组合总和）](https://www.bilibili.com/video/BV1KT4y1M7HJ/)
* [分割回文串（对应力扣题目：131.分割回文串)](https://www.bilibili.com/video/BV1c54y1e7k6)
* [关于二叉树，你该了解这些！（理论基础一网打尽）](https://www.bilibili.com/video/BV1Hy4y1t7ij)

（持续更新中....）

# 关于作者

大家好，我是程序员Carl，哈工大师兄，ACM 校赛、黑龙江省赛、东北四省赛金牌、亚洲区域赛铜牌获得者，先后在腾讯和百度从事后端技术研发，CSDN博客专家。对算法和C++后端技术有一定的见解，利用工作之余重新刷leetcode。 

**加我的微信，备注：「个人简单介绍」+「组队刷题」**， 拉你进刷题群，每天一道经典题目分析，而且题目不是孤立的，每一道题目之间都是有关系的，都是由浅入深一脉相承的，所以学习效果最好是每篇连续着看，也许之前你会某些知识点，但是一直没有把知识点串起来，这里每天一篇文章就会帮你把知识点串起来。

也欢迎找我交流，加微信备注：「个人简单介绍」 + 交流

<a name="微信"></a>
<img src="https://img-blog.csdnimg.cn/20200814140330894.png" data-img="1" width="175" height="175">

# 我的公众号

更多精彩文章持续更新，微信搜索：「代码随想录」第一时间围观，关注后回复：「666」可以获得所有算法专题原创PDF。

**每天8：35准时为你推送一篇经典面试题目，帮你梳理算法知识体系，轻松学习算法！**，并且公众号里有大量学习资源，也有我自己的学习心得和方法总结，更有上万录友们在这里打卡学习，**来看看就你知道了，一定会发现相见恨晚！**

<a name="公众号"></a>

![](./pics/公众号.png)

