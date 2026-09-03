class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for i in matrix:
            for num in i:
                flat.append(num)

        l = 0 
        r = len(flat)-1

        while l <= r:
            mid = l + (r-l)//2

            if flat[mid] == target:
                return True

            elif target > flat[mid]:
                l = mid + 1

            else:
                r = mid -1

        return False