class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) -1
        h = 0
        l=0
        length = 0
        area = 0
        
        while l < r:
            length = abs(r - l)
            h = min(height[l], height[r])

            if height[l] > height[r]:
                r-=1
            else:
                l+=1


            if length*h > area:
                area = length*h

        return area

            


            

       

