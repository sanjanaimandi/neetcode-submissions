class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            if i+1 in range(len(s)):

                val = abs(ord(s[i+1]) - ord(s[i]))
                total += val
            else:
                break
            
        return total