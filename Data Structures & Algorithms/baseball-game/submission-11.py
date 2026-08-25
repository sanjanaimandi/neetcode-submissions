class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 

        for i in range(len(operations)):
            if operations[i] == "D":
                newprod = 2 * stack[-1]
                stack.append(newprod) 
            elif operations[i] == "+":
                newnum = stack[-2] + stack[-1]
                stack.append(newnum)
            elif operations[i] == "C":
                stack.pop()
            else:
                operations[i].isdigit()
                stack.append(int(operations[i]))

        return sum(stack)


        