
"""
0017.电话号码的字母组合
# 17.电话号码的字母组合

[力扣题目链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![17.电话号码的字母组合](https://code-thinking-1253855093.file.myqcloud.com/pics/2020102916424043.png)

示例:
* 输入："23"
* 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""

from typing import List


"""回溯法
先取第一个数字的 第一个字母，然后依次取第二个数字的所有字母,...
"""

class Solution:
    def __init__(self):
        self.res:List[str] = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def combinePhonenum(self, digit:str ) -> List[str]:
        if len(digit) == 0:
            return []
        self.dfs(digit, 0, '')
        return self.res

    def dfs(self, digit, index, ans):

        # 等于数字长度，添加到结果集，并退出到上一层
        if index == len(digit):
            self.res.append( ans )
            return

        # 基础循环
        letters:str = self.letter_map[ digit[index] ]
        for s in letters:
            self.dfs(digit, index + 1, ans + s)


if __name__ == '__main__':
    f = Solution()

    print( f.combinePhonenum( "23" ) )
