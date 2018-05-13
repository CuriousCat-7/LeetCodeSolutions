class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(1, len(nums) -i):
                if nums[i] + nums[i+j] == target:
                    return [i,i+j]
        return []
