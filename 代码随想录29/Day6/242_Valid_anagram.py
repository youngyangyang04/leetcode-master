class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initialize a list to record the frequency of each letter in the alphabet
        record = [0] * 26

        # Iterate through each character in the first string (s)
        for i in s:
            # Update the count of the current character in the record list
            # by finding its relative position in the alphabet
            record[ord(i) - ord("a")] += 1

        # Iterate through each character in the second string (t)
        for i in t:
            # Decrease the count of the current character in the record list
            # Similar to the first loop, we use relative position in the alphabet
            record[ord(i) - ord("a")] -= 1

        # Check if all counts in the record list are zero
        for i in range(26):
            if record[i] != 0:
                # If any count is not zero, the strings are not anagrams
                return False

        # If all counts are zero, the strings are anagrams
        return True
