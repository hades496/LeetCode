class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mod = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        div = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        str = ''
        for i, divect in enumerate(div):
            if num >= divect:
                t = num / divect
                for _ in range(t): str += mod[i]
                num = num % divect
        return (str)
