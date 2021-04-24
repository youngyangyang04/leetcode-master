
<p align="center">
  <a href="https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ"><img src="https://img.shields.io/badge/知识星球-代码随想录-blue" alt=""></a>
  <a href="https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw"><img src="https://img.shields.io/badge/刷题-微信群-green" alt=""></a>
  <a href="https://img-blog.csdnimg.cn/20201210231711160.png"><img src="https://img.shields.io/badge/公众号-代码随想录-brightgreen" alt=""></a>
  <a href="https://space.bilibili.com/525438321"><img src="https://img.shields.io/badge/B站-代码随想录-orange" alt=""></a>
</p>

--------------------------
现在很多企业都在牛客上进行面试，**很多录友和我反馈说搞不懂牛客上输入代码的ACM模式**。

什么是ACM输入模式呢？ 就是自己构造输入数据格式，把要需要处理的容器填充好，OJ不会给你任何代码，包括include哪些函数都要自己写，最后也要自己控制返回数据的格式。

而力扣上是核心代码模式，就是把要处理的数据都已经放入容器里，可以直接写逻辑，例如这样：

```C++
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {

    }
};
```

**如果大家从一开始学习算法就一直在力扣上的话，突然切到牛客网上的ACM模式会很不适应**。

因为我上学的时候就搞ACM，在POJ（北大的在线判题系统）和ZOJ（浙大的在线判题系统）上刷过6、7百道题目了，对这种ACM模式就很熟悉。

接下来我给大家讲一下ACM模式应该如何写。

这里我拿牛客上 腾讯2020校园招聘-后台 的面试题目来举一个例子，本题我不讲解题思路，只是拿本题为例讲解ACM输入输出格式。

题目描述：

由于业绩优秀，公司给小Q放了 n 天的假，身为工作狂的小Q打算在在假期中工作、锻炼或者休息。他有个奇怪的习惯：不会连续两天工作或锻炼。只有当公司营业时，小Q才能去工作，只有当健身房营业时，小Q才能去健身，小Q一天只能干一件事。给出假期中公司，健身房的营业情况，求小Q最少需要休息几天。

输入描述:
第一行一个整数  表示放假天数
第二行 n 个数 每个数为0或1,第 i 个数表示公司在第 i 天是否营业
第三行 n 个数 每个数为0或1,第 i 个数表示健身房在第 i 天是否营业
（1为营业 0为不营业）

输出描述:
一个整数，表示小Q休息的最少天数

示例一：
输入:
4
1 1 0 0
0 1 1 0

输出:
2


这道题如果要是力扣上的核心代码模式，OJ应该直接给出如下代码：

```C++
class Solution {
public:
    int getDays(vector<int>& work, vector<int>& gym) {
        // 处理逻辑
    }
};
```

以上代码中我们直接写核心逻辑就行了，work数组，gym数组都是填好的，直接拿来用就行，处理完之后 return 结果就完事了。

那么看看ACM模式我们要怎么写呢。

ACM模式要求写出来的代码是直接可以本地运行的，所以我们需要自己写include哪些库函数，构造输入用例，构造输出用例。

拿本题来说，为了让代码可以运行，需要include这些库函数：

```C++
#include<iostream>
#include<vector>
using namespace std;
```


然后开始写主函数，来处理输入用例了，示例一 是一个完整的测试用例，一般我们测了一个用例还要测第二个用例，所以用：while(cin>>n) 来输入数据。

这里输入的n就是天数，得到天数之后，就可以来构造work数组和gym数组了。

此时就已经完成了输入用例构建，然后就是处理逻辑了，最后返回结果。

完整代码如下：

```C++
#include<iostream>
#include<vector>
using namespace std;
int main() {
    int n;
    while (cin >> n) {
        vector<int> gym(n);
        vector<int> work(n);
        for (int i = 0; i < n; i++) cin >> work[i];
        for (int i = 0; i < n; i++) cin >> gym[i];
        int result = 0;

        // 处理逻辑

        cout << result << endl;
    }
    return 0;
}
```

可以看出ACM模式要比核心代码模式多写不少代码，相对来说ACM模式更锻炼代码能力，而核心代码模式是把侧重点完全放在算法逻辑上。

**国内企业现在很多都用牛客来进行面试，所以这种ACM模式大家还有必要熟悉一下**，以免面试的时候因为输入输出搞不懂而错失offer。

如果大家有精力的话，也可以去POJ上去刷刷题，POJ是ACM选手首选OJ，输入模式也是ACM模式。


------------------------

* 微信：[程序员Carl](https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw)
* B站：[代码随想录](https://space.bilibili.com/525438321)
* 知识星球：[代码随想录](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ)

![](../pics/公众号.png)
