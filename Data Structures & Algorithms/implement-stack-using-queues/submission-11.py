

class MyStack:

    def __init__(self ):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        for _ in range(len(self.q)) :
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        num = self.q.pop()
        return num

    def top(self) -> int:
        num = self.q[-1]
        return num
        

    def empty(self) -> bool:
        if self.q:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()