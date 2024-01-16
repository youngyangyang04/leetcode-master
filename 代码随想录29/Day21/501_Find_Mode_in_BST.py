class Solution:
    def __init__(self):
        # Initialize variables to keep track of frequency and previous node
        self.maxCount = 0  # Maximum frequency
        self.count = 0  # Count of frequency
        self.pre = None  # Previous node
        self.result = []  # List to store mode(s)

    def searchBST(self, cur):
        # Recursive function for in-order traversal of the binary search tree

        if cur is None:
            return

        # Traverse the left subtree
        self.searchBST(cur.left)

        # Process the current node (middle)
        if self.pre is None:  # For the first node
            self.count = 1
        elif self.pre.val == cur.val:  # If the value is the same as the previous node
            self.count += 1
        else:  # If the value is different from the previous node
            self.count = 1
        self.pre = cur  # Update the previous node

        # Check if the count is equal to the maximum count, and add to result
        if self.count == self.maxCount:
            self.result.append(cur.val)

        # Check if the count is greater than the maximum count
        if self.count > self.maxCount:
            self.maxCount = self.count  # Update the maximum frequency
            self.result = [cur.val]  # Reset result to include the current value

        # Traverse the right subtree
        self.searchBST(cur.right)

    def findMode(self, root):
        # Entry point for finding the mode in the binary search tree
        self.count = 0
        self.maxCount = 0
        self.pre = None  # Record the previous node
        self.result = []  # Initialize result list

        # Start in-order traversal from the root
        self.searchBST(root)

        return self.result
