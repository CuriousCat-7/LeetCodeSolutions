class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        codebook = {'2':'abc', '3':'def', '4':'ghi', '5': 'jkl',
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        l = ['']
        for i in digits:
            substr = codebook[i]
            subl = []
            for j in substr:
                subl.extend([item+j for item in l])
            l = subl
        if l[0] == '':
            return []
        return l
# I should use 回溯 next time
