class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        if high == 0:
            return 0 if nums[0] >= target else 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        if nums[mid] < target:
            return (mid + 1)
        else:      
            return mid