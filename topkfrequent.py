class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        di = {i:0 for i in set(nums)}
        for i in nums:
            di[i] += 1
        sel = sorted(di.items(), key=lambda item: item[-1], reverse=True)
        sel = sel[:k]
        sel = [i[0] for i in sel]
        return sel
