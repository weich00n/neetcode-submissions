class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    # record the difference between the pushed value and the current minimum.
    def push(self, val: int) -> None:
        if self.stack and self.minStack[-1] < val:
            self.stack.append(val)
            self.minStack.append(self.minStack[-1])
        else:
            self.stack.append(val)
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        
    def top(self) -> int:
       return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
        
