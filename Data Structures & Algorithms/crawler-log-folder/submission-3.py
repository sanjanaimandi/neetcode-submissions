class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for c in logs:
            if c == "../" and depth == 0:
                depth = 0
            elif c == "../":
                depth -=1
            elif c == "./":
                depth = depth
            else:
                depth +=1

        return depth

