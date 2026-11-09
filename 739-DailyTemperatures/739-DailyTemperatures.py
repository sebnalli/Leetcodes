# Last updated: 11/8/2026, 9:21:25 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stk = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stk and temperatures[stk[-1]] < temperatures[i]:
                prev = stk.pop()
                res[prev] = i - prev

            stk.append(i)

        return res
