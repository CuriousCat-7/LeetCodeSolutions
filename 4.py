class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        idx = (m+n)/2
        nums3 = []
        if (m+n)%2 == 0:
            single = False
        else:
            single = True
        j,k = 0,0
        inf = float('Inf')
        if not single:
            for i in range(idx+1):
                try:
                    n1 = nums1[j]
                except:
                    n1 = inf
                try:
                    n2 = nums2[k]
                except:
                    n2 = inf
                if n1 < n2:
                    j += 1
                else:
                    k +=1
                if i>= idx-1:
                    nums3.append(min(n1,n2))
            return sum(nums3)/2.0
        else:
            for i in range(idx+1):
                print i, i
                try:
                    n1 = nums1[j]
                except:
                    n1 = inf
                try:
                    n2 = nums2[k]
                except:
                    n2 = inf
                if n1 < n2:
                    j += 1
                else:
                    k += 1
                if i>= idx:
                    return min(n1,n2)
