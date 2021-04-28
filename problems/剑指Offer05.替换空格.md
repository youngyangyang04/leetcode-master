<p align="center">
  <a href="https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ"><img src="https://img.shields.io/badge/知识星球-代码随想录-blue" alt=""></a>
  <a href="https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw"><img src="https://img.shields.io/badge/刷题-微信群-green" alt=""></a>
  <a href="https://img-blog.csdnimg.cn/20201210231711160.png"><img src="https://img.shields.io/badge/公众号-代码随想录-brightgreen" alt=""></a>
  <a href="https://space.bilibili.com/525438321"><img src="https://img.shields.io/badge/B站-代码随想录-orange" alt=""></a>
</p>


# 题目：剑指Offer 05.替换空格

https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

# 思路

如果想把这道题目做到极致，就不要只用额外的辅助空间了！

首先扩充数组到每个空格替换成"%20"之后的大小。

然后从后向前替换空格，也就是双指针法，过程如下：

i指向新长度的末尾，j指向旧长度的末尾。

![替换空格](https://tva1.sinaimg.cn/large/e6c9d24ely1go6qmevhgpg20du09m4qp.gif)

有同学问了，为什么要从后向前填充，从前向后填充不行么？

从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素向后移动。

**其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。**

这么做有两个好处：

1. 不用申请新数组。
2. 从后向前填充元素，避免了从前先后填充元素要来的 每次添加元素都要将添加元素之后的所有元素向后移动。

时间复杂度，空间复杂度均超过100%的用户。

<img src='https://code-thinking.cdn.bcebos.com/pics/%E5%89%91%E6%8C%87Offer05.%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.png' width=600> </img></div>

## C++代码

```C++
class Solution {
public:
    string replaceSpace(string s) {
        int count = 0; // 统计空格的个数
        int sOldSize = s.size();
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                count++;
            }
        }
        // 扩充字符串s的大小，也就是每个空格替换成"%20"之后的大小
        s.resize(s.size() + count * 2);
        int sNewSize = s.size();
        // 从后先前将空格替换为"%20"
        for (int i = sNewSize - 1, j = sOldSize - 1; j < i; i--, j--) {
            if (s[j] != ' ') {
                s[i] = s[j];
            } else {
                s[i] = '0';
                s[i - 1] = '2';
                s[i - 2] = '%';
                i -= 2;
            }
        }
        return s;
    }
};

```
时间复杂度：O(n)
空间复杂度：O(1)

此时算上本题，我们已经做了七道双指针相关的题目了分别是：

* [27.移除元素](https://mp.weixin.qq.com/s/wj0T-Xs88_FHJFwayElQlA)
* [15.三数之和](https://mp.weixin.qq.com/s/r5cgZFu0tv4grBAexdcd8A)
* [18.四数之和](https://mp.weixin.qq.com/s/nQrcco8AZJV1pAOVjeIU_g)
* [206.翻转链表](https://mp.weixin.qq.com/s/pnvVP-0ZM7epB8y3w_Njwg)
* [142.环形链表II](https://mp.weixin.qq.com/s/_QVP3IkRZWx9zIpQRgajzA)
* [344.反转字符串](https://mp.weixin.qq.com/s/X02S61WCYiCEhaik6VUpFA)

# 拓展

这里也给大家拓展一下字符串和数组有什么差别，

字符串是若干字符组成的有限序列，也可以理解为是一个字符数组，但是很多语言对字符串做了特殊的规定，接下来我来说一说C/C++中的字符串。

在C语言中，把一个字符串存入一个数组时，也把结束符 '\0'存入数组，并以此作为该字符串是否结束的标志。

例如这段代码：

```
char a[5] = "asd";
for (int i = 0; a[i] != '\0'; i++) {
}
```

在C++中，提供一个string类，string类会提供 size接口，可以用来判断string类字符串是否结束，就不用'\0'来判断是否结束。

例如这段代码:

```
string a = "asd";
for (int i = 0; i < a.size(); i++) {
}
```

那么vector< char > 和 string 又有什么区别呢？

其实在基本操作上没有区别，但是 string提供更多的字符串处理的相关接口，例如string 重载了+，而vector却没有。

所以想处理字符串，我们还是会定义一个string类型。



------------------------

* 微信：[程序员Carl](https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw)
* B站：[代码随想录](https://space.bilibili.com/525438321)
* 知识星球：[代码随想录](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ)

![](../pics/公众号.png)

