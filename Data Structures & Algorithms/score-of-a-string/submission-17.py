class Solution:
    def scoreOfString(self, s: str) -> int:
        res = []
        for i in range(len(s)-1):
            num = abs(ord(s[i]) - ord(s[i+1]))
            res.append(num)

        return sum(res)

        