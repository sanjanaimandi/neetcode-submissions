class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dicti = {}
      for word in strs:
        key = tuple(sorted(word))
        if key not in dicti:
            dicti[key] = []
        dicti[key].append(word)

      return (list(dicti.values()))



    
    
    


