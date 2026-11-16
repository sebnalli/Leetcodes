# Last updated: 2026-11-15, 11:31:45 p.m.
class Solution(object):
    def topKFrequent(self, nums, k):

        count = {}
        result = []

        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for num in nums:
            if num not in count:
                count[num] = 1
                continue

            count[num] += 1
        
        for num, freq in count.items():
            buckets[freq].append(num)

        for bucket in reversed(buckets):

            if len(result) >= k:
                break

            if not bucket:
                continue 

            result.extend(bucket)

        return result

