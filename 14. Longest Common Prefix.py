class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return("")
            
        strsArr = zip(*strs)
        out = ""
        for i, arr in enumerate(strsArr):
            if len(set(arr)) > 1:
                return(strs[0][:i])
        return(min(strs))
