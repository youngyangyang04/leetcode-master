

'''
[力扣题目链接](https://leetcode.cn/problems/longest-palindromic-substring/)

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
* 输入：s = "babad"
* 输出："bab"
* 解释："aba" 同样是符合题意的答案。

示例 2：
* 输入：s = "cbbd"
* 输出："bb"

示例 3：
* 输入：s = "a"
* 输出："a"

示例 4：
* 输入：s = "ac"
* 输出："a"
'''

# 思路：双指针

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len( s )
        left, right = 0, 0
        ans = ''
        for i in range( n ):
            left = i - 1
            right = i + 1
            while left >= 0 and s[left] == s[i]:
                left -= 1
            while right < n and s[right] == s[i]:
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # print(i, s[left+1:right],len(ans),right-left-1)
            if right-left-1 >= len(ans):
                ans = s[left+1:right]
        return ans







if __name__ == '__main__':
    for s in ["babad", 'b', 'cbbd', 'ac' ,'abbba']:
        ans = Solution().longestPalindrome( s )
        print(s, 'ans: ', ans)
