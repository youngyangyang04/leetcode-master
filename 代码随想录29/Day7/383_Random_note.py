class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #   Use list
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for char in ransomNote:
            ransom_count[ord(char) - ord("a")] += 1
        for char in magazine:
            magazine_count[ord(char) - ord("a")] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
        # The counts for all letters in the ransomNote must be less than or equal to the counts in the magazine for the method to return True
