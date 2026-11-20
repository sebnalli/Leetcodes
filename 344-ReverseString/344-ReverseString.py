# Last updated: 2026-11-19, 11:24:38 p.m.
class Solution(object):
    def reverseString(self, s):

        right = len(s) - 1
        left = 0

        while right > left:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        
        return s