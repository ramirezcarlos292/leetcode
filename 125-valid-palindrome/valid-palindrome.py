class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join([c.lower() for c in s if c.isalnum()])
        lp = 0
        rp = len(filtered)-1
        
        while lp < rp:
            if filtered[lp] != filtered[rp]:
                return False
            lp += 1
            rp -= 1
        
        return True
