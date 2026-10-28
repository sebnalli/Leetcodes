import operator

class Solution(object):
    def evalRPN(self, tokens):
        stk = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:
            if token not in ops:
                stk.append(int(token))

            else:
                b = stk.pop()
                a = stk.pop()

                stk.append(int(ops[token](a,b)))

        return stk.pop()



        


