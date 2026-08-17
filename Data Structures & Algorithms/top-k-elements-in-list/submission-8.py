class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        for i in nums:
            if i in dicti:
                dicti[i] +=1
            else:
                dicti[i] = 1

        sorted_items = sorted(dicti.items(), key=lambda pair:   pair[1], reverse=True)  

        sol = [] 

        for i in sorted_items:
            sol.append(i[0])

        return sol[0:k]

        
            

        
