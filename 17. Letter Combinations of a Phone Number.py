#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
        stack = [head, ] #初始化栈
        while stack:#当栈非空
            head = stack[-1] #获取栈顶元素
            if head.step == length: #递归终点
                res.append(head.now)
                stack.pop()
            else:
                if head._ < len(diction[digits[head.step]]): #若当前节点还能继续扩展
                    new = Solution.StackMod(head.step + 1, head.now + diction[digits[head.step]][head._])
                    head._ += 1
                    stack.append(new) #新节点入栈
                else:
                    stack.pop() #当前节点出栈
        return res
