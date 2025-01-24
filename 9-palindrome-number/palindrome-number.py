class Solution:
    def isPalindrome(self, x: int) -> bool:
        A = str(x)
        B = A[::-1]
        if A==B:
            return True
        else:
            return False
        