class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(float('-Inf'))
        left = 0
        right = len(nums)-2
        while left != right:
            mid = (left+right)/2
            if nums[mid] > nums[mid-1] and nums[mid]> nums[mid+1]:
                return mid
            if nums[mid+1] > nums[mid-1]:
                left = mid+1
            else:
                right = mid
        return left
