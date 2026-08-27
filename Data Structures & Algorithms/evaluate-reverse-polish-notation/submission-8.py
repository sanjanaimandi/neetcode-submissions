class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = ['-', '+', '*', '/']
        stack = []

        for i in tokens:
            if i in ops:
                b = int(stack.pop())
                a = int(stack.pop() )      
                if i == '-':
                    res = a-b
                    stack.append(res)
                elif i == '+':
                    res = a+b
                    stack.append(res)
                elif i == '*':
                    res = a*b
                    stack.append(res)
                else:
                    res = int(a / b)
                    stack.append(res)
            else:
                stack.append(i)

        

        return int(stack[0])


        
        