from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, value in enumerate(nums):
            if target - value in res.keys():
                return [res[target - value], i]
            else:
                res[value] = i
        return []


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    f = Solution()
    ans = f.twoSum(nums, target)
    print('ans: ', ans)
