class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into a list of words
        words = s.split()
        
        left = 0 
        right = len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        # Join the reversed words into a string with space as the separator
        return " ".join(words)