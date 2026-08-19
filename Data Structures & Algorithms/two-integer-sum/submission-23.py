class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if nums[i] not in ans:
                ans[num] = i
            else:
                return [ans[nums[i]], i]
            
            

        
        