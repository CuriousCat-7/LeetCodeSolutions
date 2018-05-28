class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        up = n
        down = 1
        while up != down:
            mid = (up + down)/2
            if isBadVersion(mid):
                up = mid
            else:
                down = mid + 1
        return up
