<p align="center">
<a href="https://www.programmercarl.com/xunlian/xunlianying.html" target="_blank">
  <img src="../pics/训练营.png" width="1000"/>
</a>
<p align="center"><strong><a href="./qita/join.md">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们受益！</strong></p>


# 右旋字符串 

力扣已经将剑指offer题目下架，所以在卡码网上给大家提供类似的题目来练习 

[卡码网题目链接](https://kamacoder.com/problempage.php?pid=1065)

字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。

例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。 

输入：输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。 

输出：输出共一行，为进行了右旋转操作后的字符串。 

样例输入： 

```
2
abcdefg 
``` 

样例输出： 

```
fgabcde
```

数据范围：1 <= k < 10000, 1 <= s.length < 10000;


## 思路

为了让本题更有意义，提升一下本题难度：**不能申请额外空间，只能在本串上操作**。 （Java不能在字符串上修改，所以使用java一定要开辟新空间）

不能使用额外空间的话，模拟在本串操作要实现右旋转字符串的功能还是有点困难的。

那么我们可以想一下上一题目[字符串：花式反转还不够！](https://programmercarl.com/0151.翻转字符串里的单词.html)中讲过，使用整体反转+局部反转就可以实现反转单词顺序的目的。


本题中，我们需要将字符串右移n位，字符串相当于分成了两个部分，如果n为2，符串相当于分成了两个部分，如图： （length为字符串长度） 

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231106170143.png)


右移n位， 就是将第二段放在前面，第一段放在后面，先不考虑里面字符的顺序，是不是整体倒叙不就行了。如图： 

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231106171557.png) 

此时第一段和第二段的顺序是我们想要的，但里面的字符位置被我们倒叙，那么此时我们在把 第一段和第二段里面的字符再倒叙一把，这样字符顺序不就正确了。 如果： 

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231106172058.png) 

其实，思路就是 通过 整体倒叙，把两段子串顺序颠倒，两个段子串里的的字符在倒叙一把，**负负得正**，这样就不影响子串里面字符的顺序了。 

整体代码如下： 

```CPP 
// 版本一
#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    int len = s.size(); //获取长度

    reverse(s.begin(), s.end()); // 整体反转
    reverse(s.begin(), s.begin() + n); // 先反转前一段，长度n
    reverse(s.begin() + n, s.end()); // 再反转后一段

    cout << s << endl;

} 
```

那么整体反正的操作放在下面，先局部反转行不行？ 

可以的，不过，要记得 控制好 局部反转的长度，如果先局部反转，那么先反转的子串长度就是 len - n，如图： 

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20231106172534.png)

代码如下： 

```CPP
// 版本二 
#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    int len = s.size(); //获取长度
    reverse(s.begin(), s.begin() + len - n); // 先反转前一段，长度len-n ，注意这里是和版本一的区别
    reverse(s.begin() + len - n, s.end()); // 再反转后一段
    reverse(s.begin(), s.end()); // 整体反转
    cout << s << endl;

}
```


## 拓展 

大家在做剑指offer的时候，会发现 剑指offer的题目是左反转，那么左反转和右反转 有什么区别呢？ 

其实思路是一样一样的，就是反转的区间不同而已。如果本题是左旋转n，那么实现代码如下： 

```CPP
#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    int len = s.size(); //获取长度
    reverse(s.begin(), s.begin() + n); //  反转第一段长度为n 
    reverse(s.begin() + n, s.end()); // 反转第二段长度为len-n 
    reverse(s.begin(), s.end());  // 整体反转
    cout << s << endl;

}
```

大家可以感受一下 这份代码和 版本二的区别， 其实就是反转的区间不同而已。 

那么左旋转的话，可以不可以先整体反转，例如想版本一的那样呢？ 

当然可以。




## 其他语言版本

### Java：



### Python: 


### Go：


### JavaScript：


### TypeScript：


### Swift:



### PHP：


### Scala:


### Rust:




<p align="center">
<a href="https://programmercarl.com/other/kstar.html" target="_blank">
  <img src="../pics/网站星球宣传海报.jpg" width="1000"/>
</a>
