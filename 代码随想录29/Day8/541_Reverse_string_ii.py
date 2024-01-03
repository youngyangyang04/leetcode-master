class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Case-I: For every 2 * k characters of that string s, reverse the first k characters, then go for another 2k chars and reverse the first k chars and go on.

        Case-II: While doing case-I, if few chars are left and those chars are not equal 2k, then if they lie in the range of k to 2k (k included), reverse the first k chars and don't do anything on other chars.

        Case-III: If there are fewer than k characters left, reverse all of them.
        """

        def reverse_substring(text):
            # Helper function to reverse a substring (implemented as a list)
            n = len(text)
            i = 0
            j = n - 1
            while i < j:
                text[i], text[j] = text[j], text[i]
                i += 1
                j -= 1
            return text

        # Convert the input string to a list for in-place modifications
        res = list(s)

        # Iterate through the string with a step of 2 * k
        for cur in range(0, len(s), 2 * k):
            # Reverse the first k characters in each 2k block
            res[cur : cur + k] = reverse_substring(res[cur : cur + k])

        # Convert the list back to a string and return the result
        return "".join(res)
