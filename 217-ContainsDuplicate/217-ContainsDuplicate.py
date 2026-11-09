# Last updated: 11/8/2026, 9:21:29 PM
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
        