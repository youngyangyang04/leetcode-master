class Solution:
    # Greedy Algorithm:
    # Install cameras from bottom to top: Skipping leaves requires the minimum installation, making it a local optimum -> global optimum
    # Install cameras on the parent nodes of leaves first, then install a camera every two layers, until the root
    # 0: Node is not covered
    # 1: Node has a camera
    # 2: Node is covered

    def minCameraCover(self, root: TreeNode) -> int:
        result = [0]  # Used to record the number of cameras installed
        if self.traversal(root, result) == 0:
            result[0] += 1

        return result[0]

    def traversal(self, cur: TreeNode, result: List[int]) -> int:
        if not cur:
            return 2

        left = self.traversal(cur.left, result)
        right = self.traversal(cur.right, result)

        # Case 1: Both left and right nodes are covered
        if left == 2 and right == 2:
            return 0

        # Case 2:
        # - left == 0 && right == 0: Neither left nor right nodes are covered
        # - left == 1 && right == 0: Left node has a camera, right node is not covered
        # - left == 0 && right == 1: Left node is not covered, right node has a camera
        # - left == 0 && right == 2: Left node is not covered, right node is covered
        # - left == 2 && right == 0: Left node is covered, right node is not covered
        if left == 0 or right == 0:
            result[0] += 1
            return 1

        # Case 3:
        # - left == 1 && right == 2: Left node has a camera, right node is covered
        # - left == 2 && right == 1: Left node is covered, right node has a camera
        # - left == 1 && right == 1: Both left and right nodes have cameras
        if left == 1 or right == 1:
            return 2
