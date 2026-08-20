class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

    


        for i in range(len(nums)-1):
            l = i+1
            r = len(nums) - 1
            if i>0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                currsum = nums[l] + nums[r]

                if -nums[i] < currsum:
                    r-=1

                elif -nums[i] > currsum:
                    l+=1

                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
                    



        return sol




            
        