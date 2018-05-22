class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n+1):
            s = ''
            if i%3 == 0:
                s += 'Fizz'
            if i%5 == 0:
                s += 'Buzz'
            if s =='':
                s = str(i)
            l.append(s)
        return l
# too simple 
