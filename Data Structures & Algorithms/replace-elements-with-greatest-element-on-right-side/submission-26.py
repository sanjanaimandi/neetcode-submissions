class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        rightmax = -1
        for i in range(len(arr)-1, -1, -1):
            ans.append(rightmax)
            rightmax = max(arr[i], rightmax)

        return ans[::-1]

        

           

           

        
