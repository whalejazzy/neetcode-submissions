class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.Min.append(val)
        elif self.Min[-1] >= val:
            self.Min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.Min[-1]:
            self.Min.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]
