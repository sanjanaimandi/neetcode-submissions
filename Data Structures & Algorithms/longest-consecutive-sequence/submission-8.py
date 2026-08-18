class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        longest = 0
        start = 0
        for i in nums_set:
            if i-1 not in nums_set:
                start = i
                length = 0
            while (start+length) in nums_set:
                length+=1
            if length > longest:
                longest = length

            

        return longest


        


        

