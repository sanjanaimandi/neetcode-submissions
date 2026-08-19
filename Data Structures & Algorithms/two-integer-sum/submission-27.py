class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in ans:
                return [ans[num], i]
            ans[nums[i]] = i
            
            

        
        