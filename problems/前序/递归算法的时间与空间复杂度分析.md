<p align="center">
  <a href="https://mp.weixin.qq.com/s/RsdcQ9umo09R6cfnwXZlrQ"><img src="https://img.shields.io/badge/PDF下载-代码随想录-blueviolet" alt=""></a>
  <a href="https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw"><img src="https://img.shields.io/badge/刷题-微信群-green" alt=""></a>
  <a href="https://space.bilibili.com/525438321"><img src="https://img.shields.io/badge/B站-代码随想录-orange" alt=""></a>
  <a href="https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ"><img src="https://img.shields.io/badge/知识星球-代码随想录-blue" alt=""></a>
</p>
<p align="center"><strong>欢迎大家<a href="https://mp.weixin.qq.com/s/tqCxrMEU-ajQumL1i8im9A">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们收益！</strong></p>


# 递归算法的时间与空间复杂度分析！

之前在[通过一道面试题目，讲一讲递归算法的时间复杂度！](https://programmercarl.com/前序/通过一道面试题目，讲一讲递归算法的时间复杂度！.html)中详细讲解了递归算法的时间复杂度，但没有讲空间复杂度。

本篇讲通过求斐波那契数列和二分法再来深入分析一波递归算法的时间和空间复杂度，细心看完，会刷新对递归的认知！


## 递归求斐波那契数列的性能分析

先来看一下求斐波那契数的递归写法。

```CPP
int fibonacci(int i) {
       if(i <= 0) return 0;
       if(i == 1) return 1;
       return fibonacci(i-1) + fibonacci(i-2);
}
```

对于递归算法来说，代码一般都比较简短，从算法逻辑上看，所用的存储空间也非常少，但运行时需要内存可不见得会少。

### 时间复杂度分析

来看看这个求斐波那契的递归算法的时间复杂度是多少呢？

在讲解递归时间复杂度的时候，我们提到了递归算法的时间复杂度本质上是要看: **递归的次数 * 每次递归的时间复杂度**。

可以看出上面的代码每次递归都是$O(1)$的操作。再来看递归了多少次，这里将i为5作为输入的递归过程 抽象成一棵递归树，如图：

![递归空间复杂度分析](https://img-blog.csdnimg.cn/20210305093200104.png)

从图中，可以看出f(5)是由f(4)和f(3)相加而来，那么f(4)是由f(3)和f(2)相加而来 以此类推。

在这棵二叉树中每一个节点都是一次递归，那么这棵树有多少个节点呢？

我们之前也有说到，一棵深度（按根节点深度为1）为k的二叉树最多可以有 2^k - 1 个节点。

所以该递归算法的时间复杂度为$O(2^n)$，这个复杂度是非常大的，随着n的增大，耗时是指数上升的。

来做一个实验，大家可以有一个直观的感受。

以下为C++代码，来测一下，让我们输入n的时候，这段递归求斐波那契代码的耗时。

```CPP
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;
using namespace chrono;
int fibonacci(int i) {
       if(i <= 0) return 0;
       if(i == 1) return 1;
       return fibonacci(i - 1) + fibonacci(i - 2);
}
void time_consumption() {
    int n;
    while (cin >> n) {
        milliseconds start_time = duration_cast<milliseconds >(
            system_clock::now().time_since_epoch()
        );

        fibonacci(n);

        milliseconds end_time = duration_cast<milliseconds >(
            system_clock::now().time_since_epoch()
        );
        cout << milliseconds(end_time).count() - milliseconds(start_time).count()
            <<" ms"<< endl;
    }
}
int main()
{
    time_consumption();
    return 0;
}
```

根据以上代码，给出几组实验数据：

测试电脑以2015版MacPro为例，CPU配置：`2.7 GHz Dual-Core Intel Core i5`

测试数据如下：

* n = 40，耗时：837 ms
* n = 50，耗时：110306 ms

可以看出，$O(2^n)$这种指数级别的复杂度是非常大的。

所以这种求斐波那契数的算法看似简洁，其实时间复杂度非常高，一般不推荐这样来实现斐波那契。

其实罪魁祸首就是这里的两次递归，导致了时间复杂度以指数上升。

```CPP
return fibonacci(i-1) + fibonacci(i-2);
```

可不可以优化一下这个递归算法呢。 主要是减少递归的调用次数。

来看一下如下代码：

```CPP
// 版本二
int fibonacci(int first, int second, int n) {
    if (n <= 0) {
        return 0;
    }
    if (n < 3) {
        return 1;
    }
    else if (n == 3) {
        return first + second;
    }
    else {
        return fibonacci(second, first + second, n - 1);
    }
}
```

这里相当于用first和second来记录当前相加的两个数值，此时就不用两次递归了。

因为每次递归的时候n减1，即只是递归了n次，所以时间复杂度是 $O(n)$。

同理递归的深度依然是n，每次递归所需的空间也是常数，所以空间复杂度依然是$O(n)$。

代码（版本二）的复杂度如下：

* 时间复杂度：$O(n)$
* 空间复杂度：$O(n)$

此时再来测一下耗时情况验证一下：

```CPP
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;
using namespace chrono;
int fibonacci_3(int first, int second, int n) {
    if (n <= 0) {
        return 0;
    }
    if (n < 3) {
        return 1;
    }
    else if (n == 3) {
        return first + second;
    }
    else {
        return fibonacci_3(second, first + second, n - 1);
    }
}

void time_consumption() {
    int n;
    while (cin >> n) {
        milliseconds start_time = duration_cast<milliseconds >(
            system_clock::now().time_since_epoch()
        );

        fibonacci_3(1, 1, n);

        milliseconds end_time = duration_cast<milliseconds >(
            system_clock::now().time_since_epoch()
        );
        cout << milliseconds(end_time).count() - milliseconds(start_time).count()
            <<" ms"<< endl;
    }
}
int main()
{
    time_consumption();
    return 0;
}

```

测试数据如下：

* n = 40，耗时：0 ms
* n = 50，耗时：0 ms

大家此时应该可以看出差距了！！

### 空间复杂度分析

说完了这段递归代码的时间复杂度，再看看如何求其空间复杂度呢，这里给大家提供一个公式：**递归算法的空间复杂度 = 每次递归的空间复杂度 * 递归深度**

为什么要求递归的深度呢？

因为每次递归所需的空间都被压到调用栈里（这是内存管理里面的数据结构，和算法里的栈原理是一样的），一次递归结束，这个栈就是就是把本次递归的数据弹出去。所以这个栈最大的长度就是递归的深度。

此时可以分析这段递归的空间复杂度，从代码中可以看出每次递归所需要的空间大小都是一样的，所以每次递归中需要的空间是一个常量，并不会随着n的变化而变化，每次递归的空间复杂度就是$O(1)$。

在看递归的深度是多少呢？如图所示：

![递归空间复杂度分析](https://img-blog.csdnimg.cn/20210305094749554.png)

递归第n个斐波那契数的话，递归调用栈的深度就是n。

那么每次递归的空间复杂度是$O(1)$， 调用栈深度为n，所以这段递归代码的空间复杂度就是$O(n)$。

```CPP
int fibonacci(int i) {
       if(i <= 0) return 0;
       if(i == 1) return 1;
       return fibonacci(i-1) + fibonacci(i-2);
}
```


最后对各种求斐波那契数列方法的性能做一下分析，如题：

![递归的空间复杂度分析](https://img-blog.csdnimg.cn/20210305095227356.png)

可以看出，求斐波那契数的时候，使用递归算法并不一定是在性能上是最优的，但递归确实简化的代码层面的复杂度。

### 二分法（递归实现）的性能分析

带大家再分析一段二分查找的递归实现。

```CPP
int binary_search( int arr[], int l, int r, int x) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binary_search(arr, l, mid - 1, x);
        return binary_search(arr, mid + 1, r, x);
    }
    return -1;
}
```

都知道二分查找的时间复杂度是$O(\log n)$，那么递归二分查找的空间复杂度是多少呢？

我们依然看 **每次递归的空间复杂度和递归的深度**

每次递归的空间复杂度可以看出主要就是参数里传入的这个arr数组，但需要注意的是在C/C++中函数传递数组参数，不是整个数组拷贝一份传入函数而是传入的数组首元素地址。

**也就是说每一层递归都是公用一块数组地址空间的**，所以 每次递归的空间复杂度是常数即：$O(1)$。

再来看递归的深度，二分查找的递归深度是logn ，递归深度就是调用栈的长度，那么这段代码的空间复杂度为 $1 * logn = O(logn)$。

大家要注意自己所用的语言在传递函数参数的时，是拷贝整个数值还是拷贝地址，如果是拷贝整个数值那么该二分法的空间复杂度就是$O(n\log n)$。


## 总结

本章我们详细分析了递归实现的求斐波那契和二分法的空间复杂度，同时也对时间复杂度做了分析。

特别是两种递归实现的求斐波那契数列，其时间复杂度截然不容，我们还做了实验，验证了时间复杂度为$O(2^n)$是非常耗时的。

通过本篇大家应该对递归算法的时间复杂度和空间复杂度有更加深刻的理解了。







-----------------------
* 作者微信：[程序员Carl](https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw)
* B站视频：[代码随想录](https://space.bilibili.com/525438321)
* 知识星球：[代码随想录](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ)
<div align="center"><img src=https://code-thinking.cdn.bcebos.com/pics/01二维码.jpg width=450> </img></div>
