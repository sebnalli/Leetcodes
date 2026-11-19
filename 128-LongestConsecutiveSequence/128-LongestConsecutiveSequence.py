# Last updated: 11/18/2026, 7:30:25 PM
class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)

        longest = 0


        for num in s:
            current = num

            if num - 1 in s:
                continue

            length = 1
            while current + 1 in s:
                current = current + 1
                length = length + 1

            if length > longest:
                longest = length
        
        return longest
