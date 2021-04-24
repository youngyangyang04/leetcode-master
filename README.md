## 一些闲话：

> 1. **介绍**：本项目是一套完整的刷题计划，旨在帮助大家少走弯路，循序渐进学算法，[关注作者](#关于作者)
> 2. **PDF版本** ： [「代码随想录」算法精讲 PDF 版本](https://mp.weixin.qq.com/s/RsdcQ9umo09R6cfnwXZlrQ) 。
> 3. **知识星球** : 面试技巧/如何选择offer/大厂内推/职场规则/简历修改/技术分享/程序人生。欢迎加入[我的知识星球](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ) 。
> 4. **转载须知** ：以下所有文章如非文首说明皆为我（[程序员Carl](https://github.com/youngyangyang04)）的原创。引用本项目文章请注明出处，发现恶意抄袭或搬运，会动用法律武器维护自己的权益。让我们一起维护一个良好的技术创作环境！

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
    * [看了这么多代码，谈一谈代码风格！](./problems/看了这么多代码，谈一谈代码风格！.md)
    * [力扣上的代码想在本地编译运行？](./problems/力扣上的代码想在本地编译运行？.md)
    * [什么是核心代码模式，什么又是ACM模式？](./problems/什么是核心代码模式，什么又是ACM模式？.md)
* 工具 
    * [一站式vim配置](https://github.com/youngyangyang04/PowerVim)
    * [保姆级Git入门教程，万字详解](https://mp.weixin.qq.com/s/Q_O0ey4C9tryPZaZeJocbA)
    * [程序员应该用什么用具来写文档？](https://mp.weixin.qq.com/s/s_hig9nioq8nT-2F7AL0SQ)

* 求职 
    * [程序员的简历应该这么写！！（附简历模板）](https://mp.weixin.qq.com/s/nCTUzuRTBo1_R_xagVszsA)
    * [BAT级别技术面试流程和注意事项都在这里了](https://mp.weixin.qq.com/s/815qCyFGVIxwut9I_7PNFw)
    * [北京有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/BKrjK4myNB-FYbMqW9f3yw)
    * [上海有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/iW4_rXQzc0fJDuSmPTUVdQ)
    * [深圳有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/3VJHF2zNohBwDBxARFIn-Q)
    * [广州有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/Ir_hQP0clbnvHrWzDL-qXg)
    * [成都有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/Y9Qg22WEsBngs8B-K8acqQ)
    * [杭州有这些互联网公司，你都知道么？](https://mp.weixin.qq.com/s/33FmPJYrOU-ygovoxIaEUw)
    
* 算法性能分析
    * [关于时间复杂度，你不知道的都在这里！](https://mp.weixin.qq.com/s/LWBfehW1gMuEnXtQjJo-sw)
    * [O(n)的算法居然超时了，此时的n究竟是多大？](https://mp.weixin.qq.com/s/73ryNsuPFvBQkt6BbhNzLA)
    * [通过一道面试题目，讲一讲递归算法的时间复杂度！](https://mp.weixin.qq.com/s/I6ZXFbw09NR31F5CJR_geQ)
    * [本周小结！（算法性能分析系列一）](https://mp.weixin.qq.com/s/5m8xDbGUeGgYJsESeg5ITQ)
    * [关于空间复杂度，可能有几个疑问？](https://mp.weixin.qq.com/s/IPv4pTD6UxKkFBkgeDCZyg)
    * [递归算法的时间与空间复杂度分析！](https://mp.weixin.qq.com/s/zLeRB-GPc3q4DG-a5cQLVw)
    * [刷了这么多题，你了解自己代码的内存消耗么？](https://mp.weixin.qq.com/s/IFZQCxJlI7-_dOC25xIOYQ)

（持续更新中.....）

## 数组 

1. [数组过于简单，但你该了解这些！](./problems/数组理论基础.md) 
2. [数组：每次遇到二分法，都是一看就会，一写就废](./problems/0704.二分查找.md)
3. [数组：就移除个元素很难么？](./problems/0027.移除元素.md)
4. [数组：滑动窗口拯救了你](https://mp.weixin.qq.com/s/UrZynlqi4QpyLlLhBPglyg)
5. [数组：这个循环可以转懵很多人！](https://mp.weixin.qq.com/s/KTPhaeqxbMK9CxHUUgFDmg)
6. [数组：总结篇](https://mp.weixin.qq.com/s/LIfQFRJBH5ENTZpvixHEmg)

## 链表

1. [关于链表，你该了解这些！](https://mp.weixin.qq.com/s/ntlZbEdKgnFQKZkSUAOSpQ)
2. [链表：听说用虚拟头节点会方便很多？](https://mp.weixin.qq.com/s/slM1CH5Ew9XzK93YOQYSjA)
3. [链表：一道题目考察了常见的五个操作！](https://mp.weixin.qq.com/s/Cf95Lc6brKL4g2j8YyF3Mg)
4. [链表：听说过两天反转链表又写不出来了？](https://mp.weixin.qq.com/s/pnvVP-0ZM7epB8y3w_Njwg)
5. [链表：删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/dai-ma-sui-xiang-lu-19-shan-chu-lian-bia-2hxt/)
5. [链表：环找到了，那入口呢？](https://mp.weixin.qq.com/s/_QVP3IkRZWx9zIpQRgajzA)
6. [链表：总结篇！](https://mp.weixin.qq.com/s/vK0JjSTHfpAbs8evz5hH8A)

## 哈希表

1. [关于哈希表，你该了解这些！](https://mp.weixin.qq.com/s/g8N6WmoQmsCUw3_BaWxHZA)
2. [哈希表：可以拿数组当哈希表来用，但哈希值不要太大](https://mp.weixin.qq.com/s/vM6OszkM6L1Mx2Ralm9Dig)
3. [哈希表：哈希值太大了，还是得用set](https://mp.weixin.qq.com/s/N9iqAchXreSVW7zXUS4BVA)
4. [哈希表：用set来判断快乐数](https://mp.weixin.qq.com/s/G4Q2Zfpfe706gLK7HpZHpA)
5. [哈希表：map等候多时了](https://mp.weixin.qq.com/s/uVAtjOHSeqymV8FeQbliJQ)
6. [哈希表：其实需要哈希的地方都能找到map的身影](https://mp.weixin.qq.com/s/Ue8pKKU5hw_m-jPgwlHcbA)
7. [哈希表：这道题目我做过？](https://mp.weixin.qq.com/s/sYZIR4dFBrw_lr3eJJnteQ)
8. [哈希表：解决了两数之和，那么能解决三数之和么？](https://mp.weixin.qq.com/s/r5cgZFu0tv4grBAexdcd8A)
9. [双指针法：一样的道理，能解决四数之和](https://mp.weixin.qq.com/s/nQrcco8AZJV1pAOVjeIU_g)
10. [哈希表：总结篇！（每逢总结必经典）](https://mp.weixin.qq.com/s/1s91yXtarL-PkX07BfnwLg)


## 字符串

1. [字符串：这道题目，使用库函数一行代码搞定](https://mp.weixin.qq.com/s/X02S61WCYiCEhaik6VUpFA)
2. [字符串：简单的反转还不够！](https://mp.weixin.qq.com/s/XGSk1GyPWhfqj2g7Cb1Vgw)
3. [字符串：替换空格](https://mp.weixin.qq.com/s/t0A9C44zgM-RysAQV3GZpg)
4. [字符串：花式反转还不够！](https://mp.weixin.qq.com/s/X3qpi2v5RSp08mO-W5Vicw)
5. [字符串：反转个字符串还有这个用处？](https://mp.weixin.qq.com/s/PmcdiWSmmccHAONzU0ScgQ)
6. [帮你把KMP算法学个通透！（理论篇）B站视频](https://www.bilibili.com/video/BV1PD4y1o7nd)
7. [帮你把KMP算法学个通透！（代码篇）B站视频](https://www.bilibili.com/video/BV1M5411j7Xx)
8. [字符串：都来看看KMP的看家本领！](https://mp.weixin.qq.com/s/Gk9FKZ9_FSWLEkdGrkecyg)
9. [字符串：KMP算法还能干这个！](https://mp.weixin.qq.com/s/lR2JPtsQSR2I_9yHbBmBuQ)
10. [字符串：前缀表不右移，难道就写不出KMP了？](https://mp.weixin.qq.com/s/p3hXynQM2RRROK5c6X7xfw)
11. [字符串：总结篇！](https://mp.weixin.qq.com/s/gtycjyDtblmytvBRFlCZJg)

## 双指针法 

双指针法基本都是应用在数组，字符串与链表的题目上

1. [数组：就移除个元素很难么？](https://mp.weixin.qq.com/s/wj0T-Xs88_FHJFwayElQlA)
2. [字符串：这道题目，使用库函数一行代码搞定](https://mp.weixin.qq.com/s/X02S61WCYiCEhaik6VUpFA)
3. [字符串：替换空格](https://mp.weixin.qq.com/s/t0A9C44zgM-RysAQV3GZpg)
4. [字符串：花式反转还不够！](https://mp.weixin.qq.com/s/X3qpi2v5RSp08mO-W5Vicw)
5. [链表：听说过两天反转链表又写不出来了？](https://mp.weixin.qq.com/s/pnvVP-0ZM7epB8y3w_Njwg)
6. [链表：环找到了，那入口呢？](https://mp.weixin.qq.com/s/_QVP3IkRZWx9zIpQRgajzA)
7. [哈希表：解决了两数之和，那么能解决三数之和么？](https://mp.weixin.qq.com/s/r5cgZFu0tv4grBAexdcd8A)
8. [双指针法：一样的道理，能解决四数之和](https://mp.weixin.qq.com/s/nQrcco8AZJV1pAOVjeIU_g)
9. [双指针法：总结篇！](https://mp.weixin.qq.com/s/_p7grwjISfMh0U65uOyCjA)

## 栈与队列

1. [栈与队列：来看看栈和队列不为人知的一面](https://mp.weixin.qq.com/s/VZRjOccyE09aE-MgLbCMjQ)
2. [栈与队列：我用栈来实现队列怎么样？](https://mp.weixin.qq.com/s/P6tupDwRFi6Ay-L7DT4NVg)
3. [栈与队列：用队列实现栈还有点别扭](https://mp.weixin.qq.com/s/yzn6ktUlL-vRG3-m5a8_Yw)
4. [栈与队列：系统中处处都是栈的应用](https://mp.weixin.qq.com/s/nLlmPMsDCIWSqAtr0jbrpQ)
5. [栈与队列：匹配问题都是栈的强项](https://mp.weixin.qq.com/s/eynAEbUbZoAWrk0ZlEugqg)
6. [栈与队列：有没有想过计算机是如何处理表达式的？](https://mp.weixin.qq.com/s/hneh2nnLT91rR8ms2fm_kw)
7. [栈与队列：滑动窗口里求最大值引出一个重要数据结构](https://mp.weixin.qq.com/s/8c6l2bO74xyMjph09gQtpA)
8. [栈与队列：求前 K 个高频元素和队列有啥关系？](https://mp.weixin.qq.com/s/8hMwxoE_BQRbzCc7CA8rng)
9. [栈与队列：总结篇！](https://mp.weixin.qq.com/s/xBcHyvHlWq4P13fzxEtkPg)

## 二叉树 

题目分类大纲如下：           
<img src='https://img-blog.csdnimg.cn/20210219190809451.png' width=600 alt='二叉树大纲'> </img></div>

1. [关于二叉树，你该了解这些！](https://mp.weixin.qq.com/s/_ymfWYvTNd2GvWvC5HOE4A)
2. [二叉树：一入递归深似海，从此offer是路人](https://mp.weixin.qq.com/s/PwVIfxDlT3kRgMASWAMGhA)
3. [二叉树：听说递归能做的，栈也能做！](https://mp.weixin.qq.com/s/c_zCrGHIVlBjUH_hJtghCg)
4. [二叉树：前中后序迭代方式的写法就不能统一一下么？](https://mp.weixin.qq.com/s/WKg0Ty1_3SZkztpHubZPRg)
5. [二叉树：层序遍历登场！](https://mp.weixin.qq.com/s/Gb3BjakIKGNpup2jYtTzog) 
6. [二叉树：你真的会翻转二叉树么？](https://mp.weixin.qq.com/s/6gY1MiXrnm-khAAJiIb5Bg)
7. [本周小结！（二叉树）](https://mp.weixin.qq.com/s/JWmTeC7aKbBfGx4TY6uwuQ)
8. [二叉树：我对称么？](https://mp.weixin.qq.com/s/Kgf0gjvlDlNDfKIH2b1Oxg)
9. [二叉树：看看这些树的最大深度](https://mp.weixin.qq.com/s/guKwV-gSNbA1CcbvkMtHBg)
10. [二叉树：看看这些树的最小深度](https://mp.weixin.qq.com/s/BH8-gPC3_QlqICDg7rGSGA)
11. [二叉树：我有多少个节点？](https://mp.weixin.qq.com/s/2_eAjzw-D0va9y4RJgSmXw)
12. [二叉树：我平衡么？](https://mp.weixin.qq.com/s/isUS-0HDYknmC0Rr4R8mww)
13. [二叉树：找我的所有路径？](https://mp.weixin.qq.com/s/Osw4LQD2xVUnCJ-9jrYxJA)
14. [还在玩耍的你，该总结啦！（本周小结之二叉树）](https://mp.weixin.qq.com/s/QMBUTYnoaNfsVHlUADEzKg)
15. [二叉树：以为使用了递归，其实还隐藏着回溯](https://mp.weixin.qq.com/s/ivLkHzWdhjQQD1rQWe6zWA)
16. [二叉树：做了这么多题目了，我的左叶子之和是多少？](https://mp.weixin.qq.com/s/gBAgmmFielojU5Wx3wqFTA)
17. [二叉树：我的左下角的值是多少？](https://mp.weixin.qq.com/s/MH2gbLvzQ91jHPKqiub0Nw)
18. [二叉树：递归函数究竟什么时候需要返回值，什么时候不要返回值？](https://mp.weixin.qq.com/s/6TWAVjxQ34kVqROWgcRFOg)
19. [二叉树：构造二叉树登场！](https://mp.weixin.qq.com/s/7r66ap2s-shvVvlZxo59xg)
20. [二叉树：构造一棵最大的二叉树](https://mp.weixin.qq.com/s/1iWJV6Aov23A7xCF4nV88w)
21. [本周小结！（二叉树系列三）](https://mp.weixin.qq.com/s/JLLpx3a_8jurXcz6ovgxtg) 
22. [二叉树：合并两个二叉树](https://mp.weixin.qq.com/s/3f5fbjOFaOX_4MXzZ97LsQ)
23. [二叉树：二叉搜索树登场！](https://mp.weixin.qq.com/s/vsKrWRlETxCVsiRr8v_hHg)
24. [二叉树：我是不是一棵二叉搜索树](https://mp.weixin.qq.com/s/8odY9iUX5eSi0eRFSXFD4Q)
25. [二叉树：搜索树的最小绝对差](https://mp.weixin.qq.com/s/Hwzml6698uP3qQCC1ctUQQ)
26. [二叉树：我的众数是多少？](https://mp.weixin.qq.com/s/KSAr6OVQIMC-uZ8MEAnGHg)
27. [二叉树：公共祖先问题](https://mp.weixin.qq.com/s/n6Rk3nc_X3TSkhXHrVmBTQ)
28. [本周小结！（二叉树系列四）](https://mp.weixin.qq.com/s/CbdtOTP0N-HIP7DR203tSg)
29. [二叉树：搜索树的公共祖先问题](https://mp.weixin.qq.com/s/Ja9dVw2QhBcg_vV-1fkiCg)
30. [二叉树：搜索树中的插入操作](https://mp.weixin.qq.com/s/lwKkLQcfbCNX2W-5SOeZEA)
31. [二叉树：搜索树中的删除操作](https://mp.weixin.qq.com/s/-p-Txvch1FFk3ygKLjPAKw)
32. [二叉树：修剪一棵搜索树](https://mp.weixin.qq.com/s/QzmGfYUMUWGkbRj7-ozHoQ)
33. [二叉树：构造一棵搜索树](https://mp.weixin.qq.com/s/sy3ygnouaZVJs8lhFgl9mw)
34. [二叉树：搜索树转成累加树](https://mp.weixin.qq.com/s/hZtJh4T5lIGBarY-lZJf6Q)
35. [二叉树：总结篇！（需要掌握的二叉树技能都在这里了）](https://mp.weixin.qq.com/s/-ZJn3jJVdF683ap90yIj4Q)
 
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
10. [回溯算法：复原IP地址](https://mp.weixin.qq.com/s/v--VmA8tp9vs4bXCqHhBuA)
11. [回溯算法：求子集问题！](https://mp.weixin.qq.com/s/NNRzX-vJ_pjK4qxohd_LtA)
12. [本周小结！（回溯算法系列二）](https://mp.weixin.qq.com/s/uzDpjrrMCO8DOf-Tl5oBGw)
13. [回溯算法：求子集问题（二）](https://mp.weixin.qq.com/s/WJ4JNDRJgsW3eUN72Hh3uQ)
14. [回溯算法：递增子序列](https://mp.weixin.qq.com/s/ePxOtX1ATRYJb2Jq7urzHQ)
15. [回溯算法：排列问题！](https://mp.weixin.qq.com/s/SCOjeMX1t41wcvJq49GhMw)
16. [回溯算法：排列问题（二）](https://mp.weixin.qq.com/s/9L8h3WqRP_h8LLWNT34YlA)
17. [本周小结！（回溯算法系列三）](https://mp.weixin.qq.com/s/tLkt9PSo42X60w8i94ViiA)
18. [本周小结！（回溯算法系列三）续集](https://mp.weixin.qq.com/s/kSMGHc_YpsqL2j-jb_E_Ag)
19. [视频来了！！带你学透回溯算法（理论篇）](https://www.bilibili.com/video/BV1cy4y167mM)
20. [视频来了！！回溯算法（力扣题目：77.组合）](https://www.bilibili.com/video/BV1ti4y1L7cv)
21. [视频来了！！回溯算法剪枝操作（力扣题目：77.组合）](https://www.bilibili.com/video/BV1wi4y157er)
22. [视频来了！！回溯算法（力扣题目：39.组合总和）](https://www.bilibili.com/video/BV1KT4y1M7HJ/)
23. [回溯算法：重新安排行程](https://mp.weixin.qq.com/s/3kmbS4qDsa6bkyxR92XCTA)
24. [回溯算法：N皇后问题](https://mp.weixin.qq.com/s/lU_QwCMj6g60nh8m98GAWg)
25. [回溯算法：解数独](https://mp.weixin.qq.com/s/eWE9TapVwm77yW9Q81xSZQ)
26. [一篇总结带你彻底搞透回溯算法！](https://mp.weixin.qq.com/s/r73thpBnK1tXndFDtlsdCQ)

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

