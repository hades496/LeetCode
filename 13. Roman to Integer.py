class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        div = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = 0
        for i, divect in enumerate(mod):
            if (s.find(divect)==0):
                while(s.find(divect)==0):
                    res+=div[i]
                    s = s[len(divect):]
        return (res)
