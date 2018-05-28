class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        pivot = left
        
        while True:
            pivalue = nums[pivot]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            storidx = left
            for i in xrange(left, right):
                if nums[i] < pivalue:
                    nums[storidx], nums[i] = nums[i], nums[storidx]
                    storidx += 1
            nums[storidx], nums[right] = nums[right], nums[storidx]
            if len(nums) - storidx > k:
                left = storidx+1
            elif len(nums) - storidx < k:
                right = storidx
            else:
                break
            pivot = left
        return nums[storidx]
