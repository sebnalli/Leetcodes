# Last updated: 2026-11-15, 10:49:07 p.m.
class Solution(object):
    def topKFrequent(self, nums, k):
        map = {}
        op = []
         
        for num in nums:
            if num not in map:
                map[num] = 1
                continue

            map[num] += 1

        sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)

        return [pair[0] for pair in sorted_items[:k]]
            