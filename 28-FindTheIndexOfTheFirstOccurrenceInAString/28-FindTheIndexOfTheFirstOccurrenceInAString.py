# Last updated: 11/8/2026, 9:21:33 PM
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        m = len(haystack)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1
        