class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                return True

        return False


