# Last updated: 11/18/2026, 6:06:41 PM
class Solution(object):
    def productExceptSelf(self, nums):

        answers = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            answers[i] = prefix
            prefix *= nums[i]
        
        suffix = 1

        for i in reversed(range(len(nums))):
            answers[i] *= suffix
            suffix *= nums[i]
        
        return answers