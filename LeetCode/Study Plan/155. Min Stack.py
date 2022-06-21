class MinStack(object):

    def __init__(self):
        
        self.stack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        current_min = self.getMin() if self.getMin() is not None else math.inf
        actual_min = val if val < current_min else current_min
        self.stack.append((val, actual_min))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
