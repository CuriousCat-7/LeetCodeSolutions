class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            if i >= m+j or nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
            else:
                i += 1
        for i in xrange(n):
            nums1.pop()
                
            
            # 应该用从last出发的方法了，最后的pop很难看
