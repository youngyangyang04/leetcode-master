<p align="center">
<a href="https://www.programmercarl.com/xunlian/xunlianying.html" target="_blank">
  <img src="../pics/训练营.png" width="1000"/>
</a>
<p align="center"><strong><a href="./qita/join.md">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们受益！</strong></p>


# 替换数字 

力扣已经将剑指offer题目下架，所以我在卡码网上给大家提供类似的题目来练习 

[卡码网题目链接](https://kamacoder.com/problempage.php?pid=1064)

给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 

例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。  

对于输入字符串 "a5b"，函数应该将其转换为 "anumberb"

输入：一个字符串 s,s 仅包含小写字母和数字字符。

输出：打印一个新的字符串，其中每个数字字符都被替换为了number 

样例输入：a1b2c3  

样例输出：anumberbnumbercnumber 

数据范围：1 <= s.length < 10000。

## 思路

如果想把这道题目做到极致，就不要只用额外的辅助空间了！ （不过使用Java刷题的录友，一定要使用辅助空间，因为Java里的string不能修改）

首先扩充数组到每个数字字符替换成 "number" 之后的大小。

例如 字符串 "a5b" 的长度为3，那么 将 数字字符变成字符串 "number" 之后的字符串为 "anumberb" 长度为 8。 

如图：  

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231030165201.png) 

然后从后向前替换数字字符，也就是双指针法，过程如下：i指向新长度的末尾，j指向旧长度的末尾。

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231030173058.png)

有同学问了，为什么要从后向前填充，从前向后填充不行么？

从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素整体向后移动。

**其实很多数组填充类的问题，其做饭都是先预先给数组扩容带填充后的大小，然后在从后向前进行操作。**

这么做有两个好处：

1. 不用申请新数组。
2. 从后向前填充元素，避免了从前向后填充元素时，每次添加元素都要将添加元素之后的所有元素向后移动的问题。

C++代码如下：

```CPP
#include<iostream>
using namespace std;
int main() {
    string s;
    while (cin >> s) {
        int count = 0; // 统计数字的个数
        int sOldSize = s.size();
        for (int i = 0; i < s.size(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                count++;
            }
        }
        // 扩充字符串s的大小，也就是每个空格替换成"number"之后的大小
        s.resize(s.size() + count * 5);
        int sNewSize = s.size();
        // 从后先前将空格替换为"number"
        for (int i = sNewSize - 1, j = sOldSize - 1; j < i; i--, j--) {
            if (s[j] > '9' || s[j] < '0') {
                s[i] = s[j];
            } else {
                s[i] = 'r';
                s[i - 1] = 'e';
                s[i - 2] = 'b';
                s[i - 3] = 'm';
                s[i - 4] = 'u';
                s[i - 5] = 'n';
                i -= 5;
            }
        }
        cout << s << endl;
    }
}


```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

此时算上本题，我们已经做了七道双指针相关的题目了分别是：

* [27.移除元素](https://programmercarl.com/0027.移除元素.html)
* [15.三数之和](https://programmercarl.com/0015.三数之和.html)
* [18.四数之和](https://programmercarl.com/0018.四数之和.html)
* [206.翻转链表](https://programmercarl.com/0206.翻转链表.html)
* [142.环形链表II](https://programmercarl.com/0142.环形链表II.html)
* [344.反转字符串](https://programmercarl.com/0344.反转字符串.html)

## 拓展

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


## 其他语言版本

### C：

### Java：


### Go：



### python：

### JavaScript:


### TypeScript：


### Swift:


### Scala:


### PHP：


### Rust:




<p align="center">
<a href="https://programmercarl.com/other/kstar.html" target="_blank">
  <img src="../pics/网站星球宣传海报.jpg" width="1000"/>
</a>
