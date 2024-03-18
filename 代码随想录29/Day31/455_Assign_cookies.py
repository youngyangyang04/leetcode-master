class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # sort child sizes (from the smallest to the largest)
        s.sort()  # sort cookie sizes
        result = 0
        index = len(s) - 1

        for i in range(len(g) - 1, -1, -1):  # range(start, stop, step)
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1
        return result
