class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.l = []
        def help(st,numl,numr):
            if numl > 0:
                s = st + '('
                help(s, numl-1, numr)
            if numr > numl:
                s = st +')'
                help(s, numl, numr-1)                
            if numl == 0 and numr == 0:
                self.l.append(st)
        help('', n, n)
        return self.l    
