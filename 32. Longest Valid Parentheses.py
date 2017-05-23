class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = [-1,]
        for i in xrange(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                top=stack[-1]
                if top>=0 and s[top]=='(':
                    stack.pop()
                    res=max(res,i-stack[-1])
                else:
                    stack[-1]=i
            # print i,stack
        return res
