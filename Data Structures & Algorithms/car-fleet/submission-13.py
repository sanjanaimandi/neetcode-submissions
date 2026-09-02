class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        sol = list(zip(position, speed))

        sorted_list = sorted(sol, key=lambda pair: pair[0])

        time = (target-sorted_list[-1][0])/sorted_list[-1][1]
        stack.append(time)
        

        for i in range(len(sorted_list)-2, -1, -1):
            if ((target-sorted_list[i][0])/sorted_list[i][1]) <= time:
                stack.pop()
            else:
                time = (target-sorted_list[i][0])/sorted_list[i][1]
            stack.append(time)
            
            
                


        return len(stack)


        