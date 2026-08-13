class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            maxi = arr[i]
            if i == len(arr)-1:
                maxi = -1
            else:
                num = max(arr[i+1:])
                maxi = num
            ans.append(maxi)

        return ans

           

        
