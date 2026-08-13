class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pas = 0
        for i in details:
            if int(i[-4:-2]) > 60:
                pas+=1
        return pas
                

        