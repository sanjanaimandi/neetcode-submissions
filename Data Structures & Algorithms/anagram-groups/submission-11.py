class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dicti = {}
      for word in strs:
        sortw = tuple(sorted(word))
        if sortw not in dicti:
            dicti[sortw] = []
        dicti[sortw].append(word)

      return list(dicti.values())



    
    
    


