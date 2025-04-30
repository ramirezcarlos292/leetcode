class Solution:
    def isThree(self, n: int) -> bool:
        lst = []
        for i in range(1, n + 1):
            if n % i == 0:
                lst.append(i)
        return len(lst) == 3
