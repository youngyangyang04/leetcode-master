<p align="center">
<a href="https://programmercarl.com/other/xunlianying.html" target="_blank">
  <img src="../pics/训练营.png" width="1000"/>
</a>
<p align="center"><strong><a href="https://mp.weixin.qq.com/s/tqCxrMEU-ajQumL1i8im9A">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们收益！</strong></p>


> 反转个字符串还有这么多用处？

# 题目：剑指Offer58-II.左旋转字符串

[力扣题目链接](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：    
输入: s = "abcdefg", k = 2   
输出: "cdefgab"      

示例 2：     
输入: s = "lrloseumgh", k = 6     
输出: "umghlrlose"        

限制：      
1 <= k < s.length <= 10000        

# 思路

为了让本题更有意义，提升一下本题难度：**不能申请额外空间，只能在本串上操作**。

不能使用额外空间的话，模拟在本串操作要实现左旋转字符串的功能还是有点困难的。


那么我们可以想一下上一题目[字符串：花式反转还不够！](https://programmercarl.com/0151.翻转字符串里的单词.html)中讲过，使用整体反转+局部反转就可以实现，反转单词顺序的目的。

这道题目也非常类似，依然可以通过局部反转+整体反转 达到左旋转的目的。

具体步骤为：

1. 反转区间为前n的子串
2. 反转区间为n到末尾的子串
3. 反转整个字符串

最后就可以得到左旋n的目的，而不用定义新的字符串，完全在本串上操作。

例如 ：示例1中 输入：字符串abcdefg，n=2

如图：

<img src='https://code-thinking.cdn.bcebos.com/pics/剑指Offer58-II.左旋转字符串.png' width=600> </img></div>

最终得到左旋2个单元的字符串：cdefgab

思路明确之后，那么代码实现就很简单了

C++代码如下：

```CPP
class Solution {
public:
    string reverseLeftWords(string s, int n) {
        reverse(s.begin(), s.begin() + n);
        reverse(s.begin() + n, s.end());
        reverse(s.begin(), s.end());
        return s;
    }
};
```
是不是发现这代码也太简单了，哈哈。

# 总结


此时我们已经反转好多次字符串了，来一起回顾一下吧。

在这篇文章[344.反转字符串](https://programmercarl.com/0344.反转字符串.html)，第一次讲到反转一个字符串应该怎么做，使用了双指针法。

然后发现[541. 反转字符串II](https://programmercarl.com/0541.反转字符串II.html)，这里开始给反转加上了一些条件，当需要固定规律一段一段去处理字符串的时候，要想想在在for循环的表达式上做做文章。

后来在[151.翻转字符串里的单词](https://programmercarl.com/0151.翻转字符串里的单词.html)中，要对一句话里的单词顺序进行反转，发现先整体反转再局部反转 是一个很妙的思路。

最后再讲到本题，本题则是先局部反转再 整体反转，与[151.翻转字符串里的单词](https://programmercarl.com/0151.翻转字符串里的单词.html)类似，但是也是一种新的思路。

好了，反转字符串一共就介绍到这里，相信大家此时对反转字符串的常见操作已经很了解了。

# 题外话

一些同学热衷于使用substr，来做这道题。
其实使用substr 和 反转 时间复杂度是一样的 ，都是O(n)，但是使用substr申请了额外空间，所以空间复杂度是O(n)，而反转方法的空间复杂度是O(1)。

**如果想让这套题目有意义，就不要申请额外空间。**


## 其他语言版本

Java：
```java
class Solution {
    public String reverseLeftWords(String s, int n) {
        int len=s.length();
        StringBuilder sb=new StringBuilder(s);
        reverseString(sb,0,n-1);
        reverseString(sb,n,len-1);
        return sb.reverse().toString();
    }
     public void reverseString(StringBuilder sb, int start, int end) {
        while (start < end) {
            char temp = sb.charAt(start);
            sb.setCharAt(start, sb.charAt(end));
            sb.setCharAt(end, temp);
            start++;
            end--;
            }
        }
}
```

```java
//解法二：空间复杂度：O(1)。用原始数组来进行反转操作
//思路为：先整个字符串反转，再反转前面的，最后反转后面 n 个
class Solution {
    public String reverseLeftWords(String s, int n) {
        char[] chars = s.toCharArray();
        reverse(chars, 0, chars.length - 1);
        reverse(chars, 0, chars.length - 1 - n);
        reverse(chars, chars.length - n, chars.length - 1);
        return new String(chars);
    }

    public void reverse(char[] chars, int left, int right) {
        while (left < right) {
            chars[left] ^= chars[right];
            chars[right] ^= chars[left];
            chars[left] ^= chars[right];
            left++;
            right--;
        }
    }
```

python: 

```python
# 方法一：可以使用切片方法
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]
```
```python    
# 方法二：也可以使用上文描述的方法，有些面试中不允许使用切片，那就使用上文作者提到的方法
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        
        return "".join(s)

```

```python
# 方法三：如果连reversed也不让使用，那么自己手写一个
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        
        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)

# 同方法二
# 时间复杂度：O(n)
# 空间复杂度：O(n)，python的string为不可变，需要开辟同样大小的list空间来修改

```

```python 3
#方法四：考虑不能用切片的情况下，利用模+下标实现
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_s = ''
        for i in range(len(s)):
            j = (i+n)%len(s)
            new_s = new_s + s[j]
        return new_s

```

Go：

```go
func reverseLeftWords(s string, n int) string {
    b := []byte(s)
    // 1. 反转前n个字符
    // 2. 反转第n到end字符
    // 3. 反转整个字符
    reverse(b, 0, n-1)
    reverse(b, n, len(b)-1)
    reverse(b, 0, len(b)-1)
    return string(b)
}
// 切片是引用传递
func reverse(b []byte, left, right int){
    for left < right{
        b[left], b[right] = b[right],b[left]
        left++
        right--
    }
}
```


JavaScript：

```javascript
var reverseLeftWords = function(s, n) {
  const length = s.length;
  let i = 0;
  while (i < length - n) {
    s = s[length - 1] + s;
    i++;
  }
  return s.slice(0, length);
};
```

版本二（在原字符串上操作）：

```js
/**
 * @param {string} s
 * @param {number} n
 * @return {string}
 */
var reverseLeftWords = function (s, n) {
    /** Utils */
    function reverseWords(strArr, start, end) {
        let temp;
        while (start < end) {
            temp = strArr[start];
            strArr[start] = strArr[end];
            strArr[end] = temp;
            start++;
            end--;
        }
    }
    /** Main code */
    let strArr = s.split('');
    let length = strArr.length;
    reverseWords(strArr, 0, length - 1);
    reverseWords(strArr, 0, length - n - 1);
    reverseWords(strArr, length - n, length - 1);
    return strArr.join('');
};
```

TypeScript：

```typescript
function reverseLeftWords(s: string, n: number): string {
    /** Utils */
    function reverseWords(strArr: string[], start: number, end: number): void {
        let temp: string;
        while (start < end) {
            temp = strArr[start];
            strArr[start] = strArr[end];
            strArr[end] = temp;
            start++;
            end--;
        }
    }
    /** Main code */
    let strArr: string[] = s.split('');
    let length: number = strArr.length;
    reverseWords(strArr, 0, length - 1);
    reverseWords(strArr, 0, length - n - 1);
    reverseWords(strArr, length - n, length - 1);
    return strArr.join('');
};
```
方法二:
```typescript
// 拼接两个字符串，截取符合要求的部分
function reverseLeftWords(s: string, n: number): string {
    return (s+s).slice(n,s.length+n);
};
```

Swift:

```swift
func reverseLeftWords(_ s: String, _ n: Int) -> String {
    var ch = Array(s)
    let len = ch.count
    // 反转区间[0, n - 1]
    reverseString(&ch, startIndex: 0, endIndex: n - 1)
    // 反转区间[n, len - 1]
    reverseString(&ch, startIndex: n, endIndex: len - 1)
    // 反转区间[0, len - 1]，也就是整个字符串反转
    reverseString(&ch, startIndex: 0, endIndex: len - 1)
    return String(ch)
}

func reverseString(_ s: inout [Character], startIndex: Int, endIndex: Int)  {
    var start = startIndex
    var end = endIndex
    while start < end {
        (s[start], s[end]) = (s[end], s[start])
        start += 1
        end -= 1
    }
}
```


### PHP

```php
function reverseLeftWords($s, $n) {
    $this->reverse($s,0,$n-1); //反转区间为前n的子串
    $this->reverse($s,$n,strlen($s)-1); //反转区间为n到末尾的子串
    $this->reverse($s,0,strlen($s)-1); //反转整个字符串
    return $s;
}

// 按指定进行翻转 【array、string都可】
function reverse(&$s, $start, $end) {
    for ($i = $start, $j = $end; $i < $j; $i++, $j--) {
        $tmp = $s[$i];
        $s[$i] = $s[$j];
        $s[$j] = $tmp;
    }
}
```


Scala:

```scala
object Solution {
  def reverseLeftWords(s: String, n: Int): String = {
    var str = s.toCharArray // 转换为Array
    // abcdefg => ba cdefg 
    reverseString(str, 0, n - 1)
    // ba cdefg => ba gfedc
    reverseString(str, n, str.length - 1)
    // ba gfedc => cdefgab
    reverseString(str, 0, str.length - 1)
    // 最终返回，return关键字可以省略
    new String(str)
  }
  // 翻转字符串
  def reverseString(s: Array[Char], start: Int, end: Int): Unit = {
    var (left, right) = (start, end)
    while (left < right) {
      var tmp = s(left)
      s(left) = s(right)
      s(right) = tmp
      left += 1
      right -= 1
    }
  }
}
```

Rust:

```Rust
impl Solution {
    pub fn reverse(s: &mut Vec<char>, mut begin: usize, mut end: usize){
        while begin < end {
            let temp = s[begin];
            s[begin] = s[end];
            s[end] = temp;
            begin += 1;
            end -= 1;
        }
    }
    pub fn reverse_left_words(s: String, n: i32) -> String {
        let len = s.len();
        let mut s = s.chars().collect::<Vec<char>>();
        let n = n as usize;
        Self::reverse(&mut s, 0, n - 1);
        Self::reverse(&mut s, n, len - 1);
        Self::reverse(&mut s, 0, len - 1);
        s.iter().collect::<String>()
    }
}
```



<p align="center">
<a href="https://programmercarl.com/other/kstar.html" target="_blank">
  <img src="../pics/网站星球宣传海报.jpg" width="1000"/>
</a>
