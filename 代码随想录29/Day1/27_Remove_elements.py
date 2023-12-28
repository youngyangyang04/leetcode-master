class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # fast pointer: obtains the elements in the new nums
        # slow pointer: updates the position of the new nums
        slowIndex = 0
        fastIndex = 0
        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
            fastIndex += 1
        return slowIndex
