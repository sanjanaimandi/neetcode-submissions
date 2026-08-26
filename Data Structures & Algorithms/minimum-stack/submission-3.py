class MinStack:

    def __init__(self):
        self.s = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        num = self.s[-1]
        return num
        

    def getMin(self) -> int:
        min = self.s[0]
        for i in self.s:
            if i < min:
                min = i
        return min
        
