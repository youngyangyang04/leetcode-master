class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If the character is an opening bracket, push it onto the stack.
            if char in mapping.values():
                stack.append(char)
            # If the character is a closing bracket, check for a matching opening bracket on the stack.
            elif char in mapping.keys():
                # If the stack is empty or the top element does not match the corresponding opening bracket, return False.
                if not stack or stack.pop() != mapping[char]:
                    return False

        # The string is valid if the stack is empty, meaning all opening brackets have matching closing brackets.
        return not stack
