class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Initialize an array to store the last occurrence index of each character
        hash_map = [0] * 26
        result = []  # List to store the lengths of partitions

        # Populate the hash_map with the last occurrence index of each character
        for i in range(len(s)):
            hash_map[ord(s[i]) - ord("a")] = i

        left, right = 0, 0

        # Iterate through the string to find partitions
        for i in range(len(s)):
            # Update the rightmost index for the current character
            right = max(right, hash_map[ord(s[i]) - ord("a")])

            # If the current index is equal to the rightmost index
            if i == right:
                # Calculate the length of the current partition and append to the result
                result.append(right - left + 1)
                # Move the left pointer to the next index
                left = i + 1

        return result
