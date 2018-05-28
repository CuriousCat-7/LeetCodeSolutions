class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        up = len(nums)-1
        down = 0
        i = 0
        while i <= up:
            if nums[i] == 0:
                nums[i], nums[down] = nums[down], nums[i]
                down += 1
            elif nums[i] == 2:
                nums[i], nums[up] = nums[up], nums[i]
                up -= 1
                i -= 1
            i += 1
        
            
