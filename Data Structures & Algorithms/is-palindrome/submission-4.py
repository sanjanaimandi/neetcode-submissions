class Solution:
    def isPalindrome(self, s: str) -> bool:
        sol = ""
        for char in s:
            if char.isalnum():
                sol += char.lower()
            else:
                continue
            
        
        if sol==sol[::-1]:
            return True
        
        return False