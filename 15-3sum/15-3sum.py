# Last updated: 2026-11-25, 1:34:15 a.m.
class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        op = []

        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            target = -nums[i]

            left = i+1
            right = len(nums) - 1

            while left < right:
                
                sum = nums[left] + nums[right]

                if nums[left] + nums[right] == target:
                    op.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                elif sum < target :
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
        return op

        