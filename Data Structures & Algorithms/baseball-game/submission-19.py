class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                a = stack[-2]
                b = stack[-1]
                stack.append(a+b)

            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                b = stack[-1]
                stack.append(int(2*b))

            else:
                stack.append(int(operations[i]))

        return sum(stack)
