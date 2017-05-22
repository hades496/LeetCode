class Solution(object):
    class StackMod:
        def __init__(self, step, now, _=0):
            self.step = step
            self.now = now
            self._ = _

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        if length == 0: return []
        diction = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        head = Solution.StackMod(0, '', 0)
        stack = [head, ]
        while stack:
            head = stack[-1]
            if head.step == length:
                res.append(head.now)
                stack.pop()
            else:
                if head._ < len(diction[digits[head.step]]):
                    new = Solution.StackMod(head.step + 1, head.now + diction[digits[head.step]][head._])
                    head._ += 1
                    stack.append(new)
                else:
                    stack.pop()
        return res
