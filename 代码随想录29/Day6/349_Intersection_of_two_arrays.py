class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v = set()  # Sets are unordered collections of unique elements.
        nums1 = set(nums1)
        for i in nums1:
            if i in nums2:
                v.add(i)
        return list(v)
