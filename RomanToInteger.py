    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    summ = 0
    s = []
    while i < len(d):
        if d[i] < d[i+1]:
            summ = d[i+1] - d[i]
            i += 1
        else:
            summ += d[i]
            i += 1
    return summ
        
