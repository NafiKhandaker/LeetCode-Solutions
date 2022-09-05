class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums_hash = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            ind = nums_hash.get(target - num)
            if ind and ind != i:
                return [i, ind]
            
        return "No solution"
        
                
        
