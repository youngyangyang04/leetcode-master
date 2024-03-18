class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)  # Initialize result list with -1s
        stack = [0]  # Initialize stack with the index of the first element of nums2

        # Iterate through nums2 starting from the second element
        for i in range(1, len(nums2)):
            # Case 1 and Case 2
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(
                    i
                )  # If the current element is less than or equal to the top of the stack, append its index to the stack
            # Case 3
            else:
                # While the stack is not empty and the current element is greater than the element at the index represented by the top of the stack
                while stack and nums2[i] > nums2[stack[-1]]:
                    # If the element at the top of the stack exists in nums1
                    if nums2[stack[-1]] in nums1:
                        # Find the index of the element in nums1 and update the result at that index with the current element
                        index = nums1.index(nums2[stack[-1]])
                        result[index] = nums2[i]
                    stack.pop()  # Pop the index from the stack
                stack.append(i)  # Append the current index to the stack

        return result  # Return the result list
