class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = 0
        started = False

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if started==False:
                    continue
                else:
                    break
            else:
                num+=1
                started=True

        return num
        