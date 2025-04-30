class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxx, minn= max(nums), min(nums)
        import math
        return math.gcd(maxx, minn)
