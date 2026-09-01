class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans.append(rightMax)
            rightMax = max(arr[i], rightMax)
        return ans[::-1]    
                

           

        
