# Last updated: 2026-11-20, 9:18:54 p.m.
class Solution(object):
    def maxProfit(self, prices):

        lowest = prices[0]
        best = 0

        for price in prices:

            lowest = min(lowest, price)
            
            net = price - lowest
            best = max(best, net)
        
        return best
            
            
        