class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        map = {')':'(', '}':'{', ']':'['}
        stk = []

        for p in s:
            if p in map:
                if stk and stk[-1] == map[p]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(p)
        return True if not stk else False

             
