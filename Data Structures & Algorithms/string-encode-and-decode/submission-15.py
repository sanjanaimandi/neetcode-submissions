class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += "#"
            res += i

        return res
    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
        neww = 0

        while pos < len(s):
            if s[pos] == "#":
                skip = int(s[neww:pos])
                word = s[pos+1:pos+1+skip]
                res.append(word)
                
                neww = pos+1+skip
                pos = neww
                
            else:
                pos+=1
            
        
        return res



