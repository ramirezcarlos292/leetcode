class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for idx, item in enumerate(nums):
            #is incoming item already in dict_values
            #if yes, return true
            if item in map:
                return True
            #if not, add to dict_values
            map[item] = idx
        return False
            
                