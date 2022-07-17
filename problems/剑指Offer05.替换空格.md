<p align="center">
<a href="https://programmercarl.com/other/kstar.html" target="_blank">
  <img src="https://code-thinking-1253855093.file.myqcloud.com/pics/20210924105952.png" width="1000"/>
</a>
<p align="center"><strong><a href="https://mp.weixin.qq.com/s/tqCxrMEU-ajQumL1i8im9A">参与本项目</a>，贡献其他语言版本的代码，拥抱开源，让更多学习算法的小伙伴们收益！</strong></p>


# 题目：剑指Offer 05.替换空格

[力扣题目链接](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)

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

<img src='https://code-thinking.cdn.bcebos.com/pics/剑指Offer05.替换空格.png' width=600> </img></div>

C++代码如下：

```CPP
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

* 时间复杂度：O(n)
* 空间复杂度：O(1)

此时算上本题，我们已经做了七道双指针相关的题目了分别是：

* [27.移除元素](https://programmercarl.com/0027.移除元素.html)
* [15.三数之和](https://programmercarl.com/0015.三数之和.html)
* [18.四数之和](https://programmercarl.com/0018.四数之和.html)
* [206.翻转链表](https://programmercarl.com/0206.翻转链表.html)
* [142.环形链表II](https://programmercarl.com/0142.环形链表II.html)
* [344.反转字符串](https://programmercarl.com/0344.反转字符串.html)

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


## 其他语言版本

C：
```C
char* replaceSpace(char* s){
    //统计空格数量
    int count = 0;
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == ' ') {
            count++;
        }
    }

    //为新数组分配空间
    int newLen = len + count * 2;
    char* result = malloc(sizeof(char) * newLen + 1);
    //填充新数组并替换空格
    for (int i = len - 1, j = newLen - 1; i >= 0; i--, j--) {
        if (s[i] != ' ') {
            result[j] = s[i];
        } else {
            result[j--] = '0';
            result[j--] = '2';
            result[j] = '%';
        }
    }
    result[newLen] = '\0';

    return result;
}
```


Java：
```Java
//使用一个新的对象，复制 str，复制的过程对其判断，是空格则替换，否则直接复制，类似于数组复制
public static String replaceSpace(StringBuffer str) {
        if (str == null) {
            return null;
        }
		//选用 StringBuilder 单线程使用，比较快，选不选都行
        StringBuilder sb = new StringBuilder();
		//使用 sb 逐个复制 str ，碰到空格则替换，否则直接复制
        for (int i = 0; i < str.length(); i++) {
		//str.charAt(i) 为 char 类型，为了比较需要将其转为和 " " 相同的字符串类型
        //if (" ".equals(String.valueOf(str.charAt(i)))){
            if (s.charAt(i) == ' ') {
                sb.append("%20");
            } else {
                sb.append(str.charAt(i));
            }
        }
        return sb.toString();
    }

//方式二：双指针法
public String replaceSpace(String s) {
    if(s == null || s.length() == 0){
        return s;
    }
    //扩充空间，空格数量2倍
    StringBuilder str = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
        if(s.charAt(i) == ' '){
            str.append("  ");
        }
    }
    //若是没有空格直接返回
    if(str.length() == 0){
        return s;
    }
    //有空格情况 定义两个指针
    int left = s.length() - 1;//左指针：指向原始字符串最后一个位置
    s += str.toString();
    int right = s.length()-1;//右指针：指向扩展字符串的最后一个位置
    char[] chars = s.toCharArray();
    while(left>=0){
        if(chars[left] == ' '){
            chars[right--] = '0';
            chars[right--] = '2';
            chars[right] = '%';
        }else{
            chars[right] = chars[left];
        }
        left--;
        right--;
    }
    return new String(chars);
}
```


Go：
```go
// 遍历添加
func replaceSpace(s string) string {
    b := []byte(s)
    result := make([]byte, 0)
    for i := 0; i < len(b); i++ {
        if b[i] == ' ' {
            result = append(result, []byte("%20")...)
        } else {
            result = append(result, b[i])
        }
    }
    return string(result)
}

// 原地修改
func replaceSpace(s string) string {
    b := []byte(s)
    length := len(b)
    spaceCount := 0
    // 计算空格数量
    for _, v := range b {
        if v == ' ' {
            spaceCount++
        }
    }
    // 扩展原有切片
    resizeCount := spaceCount * 2
    tmp := make([]byte, resizeCount)
    b = append(b, tmp...)
    i := length - 1
    j := len(b) - 1
    for i >= 0 {
        if b[i] != ' ' {
            b[j] = b[i]
            i--
            j--
        } else {
            b[j] = '0'
            b[j-1] = '2'
            b[j-2] = '%'
            i--
            j = j - 3
        }
    }
    return string(b)
}
```




python：
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        
        res = list(s)
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        res.extend([' '] * counter * 2)
        
        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(res) - 1
        
        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                # [right - 2, right), 左闭右开
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)
            
```

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        # method 1 - Very rude
        return "%20".join(s.split(" "))

        # method 2 - Reverse the s when counting in for loop, then update from the end.
        n = len(s)
        for e, i in enumerate(s[::-1]):
            print(i, e)
            if i == " ":
                s = s[: n - (e + 1)] + "%20" + s[n - e:]
            print("")
        return s
```

javaScript:

```js
/**
 * @param {string} s
 * @return {string}
 */
 var replaceSpace = function(s) {
   // 字符串转为数组
  const strArr = Array.from(s);
  let count = 0;

  // 计算空格数量
  for(let i = 0; i < strArr.length; i++) {
    if (strArr[i] === ' ') {
      count++;
    }
  }

  let left = strArr.length - 1;
  let right = strArr.length + count * 2 - 1;

  while(left >= 0) {
    if (strArr[left] === ' ') {
      strArr[right--] = '0';
      strArr[right--] = '2';
      strArr[right--] = '%';
      left--;
    } else {
      strArr[right--] = strArr[left--];
    }
  }

  // 数组转字符串
  return strArr.join('');
};
```

TypeScript：

```typescript
function replaceSpace(s: string): string {
    let arr: string[] = s.split('');
    let spaceNum: number = 0;
    let oldLength: number = arr.length;
    for (let i = 0; i < oldLength; i++) {
        if (arr[i] === ' ') {
            spaceNum++;
        }
    }
    arr.length = oldLength + 2 * spaceNum;
    let cur: number = oldLength - 1;
    for (let i = arr.length - 1; i >= 0; i--, cur--) {
        if (arr[cur] !== ' ') {
            arr[i] = arr[cur]
        } else {
            arr[i] = '0';
            arr[--i] = '2';
            arr[--i] = '%';
        }
    }
    return arr.join('');
};
```

Swift:

```swift
func replaceSpace(_ s: String) -> String {
    var strArr = Array(s)
    var count = 0

    // 统计空格的个数
    for i in strArr {
        if i == " " {
            count += 1
        }
    }
    // left 指向旧数组的最后一个元素
    var left = strArr.count - 1
    // right 指向扩容后数组的最后一个元素（这里还没对数组进行实际上的扩容）
    var right = strArr.count + count * 2 - 1

    // 实际对数组扩容
    for _ in 0..<(count * 2) {
        strArr.append(" ")
    }

    while left < right {
        if strArr[left] == " " {
            strArr[right] = "0"
            strArr[right - 1] = "2"
            strArr[right - 2] = "%"
            left -= 1
            right -= 3
        } else {
            strArr[right] = strArr[left]
            left -= 1
            right -= 1
        }
    }

    return String(strArr)
}
```

Scala:

方式一: 双指针
```scala
object Solution {
  def replaceSpace(s: String): String = {
    var count = 0
    s.foreach(c => if (c == ' ') count += 1) // 统计空格的数量
    val sOldSize = s.length // 旧数组字符串长度
    val sNewSize = s.length + count * 2 // 新数组字符串长度
    val res = new Array[Char](sNewSize) // 新数组
    var index = sNewSize - 1 // 新数组索引
    // 逆序遍历
    for (i <- (0 until sOldSize).reverse) {
      if (s(i) == ' ') {
        res(index) = '0'
        index -= 1
        res(index) = '2'
        index -= 1
        res(index) = '%'
      } else {
        res(index) = s(i)
      }
      index -= 1
    }
    res.mkString
  }
}
```
方式二: 使用一个集合，遇到空格就添加%20
```scala
object Solution {
  import scala.collection.mutable.ListBuffer
  def replaceSpace(s: String): String = {
    val res: ListBuffer[Char] = ListBuffer[Char]()
    for (i <- s.indices) {
      if (s(i) == ' ') {
        res += '%'
        res += '2'
        res += '0'
      }else{
        res += s(i)
      }
    }
    res.mkString
  }
}
```
方式三: 使用map
```scala
object Solution {
  def replaceSpace(s: String): String = {
    s.map(c => if(c == ' ') "%20" else c).mkString
  }
  }
```


PHP：
```php
function replaceSpace($s){
    $sLen = strlen($s);
    $moreLen = $this->spaceLen($s) * 2;

    $head = $sLen - 1;
    $tail = $sLen + $moreLen - 1;

    $s = $s . str_repeat(' ', $moreLen);
    while ($head != $tail) {
        if ($s[$head] == ' ') {
            $s[$tail--] = '0';
            $s[$tail--] = '2';
            $s[$tail] = '%';
        } else {
            $s[$tail] = $s[$head];
        }
        $head--;
        $tail--;
    }
    return $s;
}
// 统计空格个数
function spaceLen($s){
    $count = 0;
    for ($i = 0; $i < strlen($s); $i++) {
        if ($s[$i] == ' ') {
            $count++;
        }
    }
    return $count;
}
```

Rust

```Rust
impl Solution {
    pub fn replace_space(s: String) -> String {
        let mut len: usize = s.len();
        let mut s = s.chars().collect::<Vec<char>>();
        let mut count = 0;
        for i in &s {
            if i.is_ascii_whitespace() {
                count += 1;
            }
        }
        let mut new_len = len + count * 2;
        s.resize(new_len, ' ');
        while len < new_len {
            len -= 1;
            new_len -= 1;
            if s[len].is_ascii_whitespace() {
                s[new_len] = '0';
                s[new_len - 1] = '2';
                s[new_len - 2] = '%';
                new_len -= 2;
            }
            else { s[new_len] = s[len] }
        }
        s.iter().collect::<String>()
    }
}
```


-----------------------
<div align="center"><img src=https://code-thinking.cdn.bcebos.com/pics/01二维码一.jpg width=500> </img></div>
