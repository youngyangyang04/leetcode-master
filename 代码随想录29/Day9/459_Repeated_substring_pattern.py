class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False

        #  Create a circularly shifted version of the string
        ss = s[1:] + s[:-1]

        # Print the result of finding the original string in the shifted version (for debugging)
        print(ss.find(s))

        # Return True if the original string is found in the shifted version, otherwise return False
        return ss.find(s) != -1


# print(Solution().repeatedSubstringPattern(s="abab"))
