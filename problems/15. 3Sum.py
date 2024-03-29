from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = nums[left] + nums[right] + num
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


print(Solution().threeSum([-2, 0, 0, 2, 2]))
