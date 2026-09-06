class MinStack:

    def __init__(self):
        self.s = []
        self.minimum = []
        self.pointer = -1


    def push(self, val: int) -> None:
        self.pointer = self.pointer + 1 
        self.s.append(val)

        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val, self.minimum[-1]))

    def pop(self) -> None:
        val = self.s[self.pointer]
        self.s.pop()
        self.pointer = self.pointer - 1
        self.minimum.pop()
        return val

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

