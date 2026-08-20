class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in sol:
                return [sol[diff]+1, i+1]
            else:  
                sol[numbers[i]] = i

        return 






            

        