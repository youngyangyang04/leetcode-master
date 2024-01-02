class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Prune the search if the current element is greater than the target
            if nums[i] > target and nums[i] > 0 and target > 0:
                break

            # Skip duplicates to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate over each element after the current element
            for j in range(i + 1, len(nums)):
                # Prune the search if the sum of current and next elements is greater than the target
                if nums[j] + nums[i] > target and target > 0:
                    break

                # Skip duplicates to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Initialize two pointers for the remaining part of the array
                left, right = j + 1, len(nums) - 1

                # Explore combinations of elements using two pointers
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        # Found a quadruplet with the target sum, add it to the result
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates in the left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicates in the left
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicates in the right

                        left += 1
                        right -= 1

                    # Adjust pointers based on the comparison with the target sum
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return result
