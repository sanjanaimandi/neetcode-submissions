class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in sol:
                return [sol[val], i]
            sol[nums[i]] = i
            