class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        self.nums = nums
        self.re = [-1,-1]
        self.target = target
        def helper(start,end):
            if start > end:
                return
            while start <= end:
                mid = (start + end)/2
                val = self.nums[mid]
                if val == self.target:
                    if self.re[0] == -1:
                        self.re[0] = mid
                        self.re[1] = mid
                        helper(start, mid-1)
                        helper(mid+1, end)
                        break
                    if mid < self.re[0]:
                        self.re[0] = mid
                        helper(start, mid-1)
                        break
                    if mid > self.re[1]:
                        self.re[1] = mid
                        helper(mid+1, end)
                        break
                elif val < self.target:
                    start = mid + 1
                elif val > self.target:
                    end = mid - 1
        helper(0, len(self.nums)-1)
        return self.re
            
                    
                        
                    
           # 96.76%!!!!!!! 
