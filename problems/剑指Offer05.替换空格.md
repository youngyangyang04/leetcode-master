## 题目地址 
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/


## 思路 

如果想把这道题目做到极致，就不要只用额外的辅助空间，先扩充数组到每个空格替换成"%20"之后的大小
然后从后向前替换空格


## C++代码 

时间复杂度，空间复杂度均超过100%的用户 

```
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
        s.resize(s.size() + count * 2); // 扩充字符串s的大小，也就是每个空格替换成"%20"之后的大小
        int sNewSize = s.size();
        // 从后先前将空格替换为"%20"
        for (int i = sNewSize - 1, j = sOldSize - 1; i >= 0, j >= 0; i--, j--) {
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
> 笔者在先后在腾讯和百度从事技术研发多年，利用工作之余重刷leetcode，本文  [GitHub](https://github.com/youngyangyang04/leetcode-master )：https://github.com/youngyangyang04/leetcode-master 已经收录，欢迎star，fork，共同学习，一起进步。
