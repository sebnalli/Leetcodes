class Solution(object):
    def isAnagram(self, s, t):
        d = {}

        if len(t) != len(s):
            return False

        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1

        for v in d.values():
            if v > 0:
                return False

        return True


        