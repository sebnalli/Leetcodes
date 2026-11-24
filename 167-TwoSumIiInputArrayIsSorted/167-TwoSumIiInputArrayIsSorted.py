# Last updated: 2026-11-23, 7:47:53 p.m.
class Solution(object):
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1

        while left < right:

            if numbers[left] + numbers[right] == target:
                left += 1
                right += 1

                return [left, right]

            sum = numbers[left] + numbers[right]

            if target >= sum:
                left += 1
            else:
                right -= 1
