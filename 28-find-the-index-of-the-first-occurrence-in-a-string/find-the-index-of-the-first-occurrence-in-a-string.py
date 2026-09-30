class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        m = len(haystack)

        if m == 0:
            return -1
        if haystack == needle:
            return 0
            
        for i, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i:i + n] == needle:
                    return i

        return -1
        