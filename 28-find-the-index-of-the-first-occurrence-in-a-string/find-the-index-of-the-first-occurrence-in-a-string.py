class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        l = len(needle)

        for i, char in enumerate(haystack):
                if haystack[i:i + l] == needle:
                    return i

        return -1
        