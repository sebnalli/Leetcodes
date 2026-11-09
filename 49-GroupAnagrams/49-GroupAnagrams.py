# Last updated: 11/8/2026, 9:53:42 PM
class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            key = "".join(sorted(word))

            d.setdefault(key, []).append(word)
        
        return list(d.values())