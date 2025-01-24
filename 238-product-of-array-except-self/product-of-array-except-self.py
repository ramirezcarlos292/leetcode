class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lm = [1] * l
        rm = [1] * l
        result = []
        next = nums[0]
        # calculate all right multiplications and append to an array
        for i in range(1, l):
            lm[i] = lm[i-1] * next
            next = nums[i]     
        # calculate all left multiplications and append to an array
        for i in range(l - 2, -1, -1):
            rm[i] = rm[i+1] * nums[i+1]
        
        # mutiply element wise the elements and return them
        for i in range(l):
            result.append(lm[i]*rm[i])
        
        return result