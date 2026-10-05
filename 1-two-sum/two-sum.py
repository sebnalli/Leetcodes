class Solution(object):
    def twoSum(self, nums, target):

        m = {}
        op = []

        for i in range(len(nums)):
            if target - nums[i] in m:
                op.append(m[target - nums[i]])
                op.append(i)
                return op
            else:
                m[nums[i]] = i
                
                
            
        