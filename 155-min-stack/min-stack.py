class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')
    def push(self, value: int) -> None:
        val = value
        if not self.stack:
            self.mini = val
            self.stack.append(val)
        else:
            if val < self.mini:
                # Store modified value in stack
                self.stack.append(2 * val - self.mini)
                self.mini = val
            else:
                self.stack.append(val)
    def pop(self) -> None:
        if not self.stack:
            return
        el = self.stack.pop()
        if el < self.mini:
            # Retrieve the original minimum value before the current one
            self.mini = 2 * self.mini - el
    def top(self) -> int:
        if not self.stack:
            return -1
        el = self.stack[-1]
        if el < self.mini:
            return self.mini
        return el
    def getMin(self) -> int:
        return self.mini




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()