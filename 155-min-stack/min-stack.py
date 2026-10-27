class MinStack(object):

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, value):
        self.stk.append(value)

        if not self.min_stk or value <= self.min_stk[-1]:
            self.min_stk.append(value)
        
    def pop(self):
        value = self.stk.pop() 

        if value == self.min_stk[-1]:
            self.min_stk.pop()
        
    def top(self):
        return self.stk[-1]
        

    def getMin(self):
        return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()