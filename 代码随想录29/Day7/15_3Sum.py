class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return result  # Return an empty list if the current element is greater than 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets

            # Initialize left and right pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1  # Move the right pointer to decrease the sum
                elif current_sum < 0:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates in the left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates in the right

                    left += 1
                    right -= 1

        return result
