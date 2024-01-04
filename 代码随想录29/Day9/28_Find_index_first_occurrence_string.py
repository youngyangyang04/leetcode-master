class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m):
            if haystack[i : i + n] == needle:
                return i
        return -1
