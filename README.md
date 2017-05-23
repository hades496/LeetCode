# LeetCode  
- My LeetCode solution List  

### 4. Longest Substring Without Repeating Characters：  
- Using the dict[] to record the last position of each letter.  

### 5. Longest Palindromic Substring:  
- Learning "Manacher" algorithm.  
  - tips:substr(start_position,lens)  
  
### 6. ZigZag Conversion:  
- Find the Regulation.  

### 11. Container With Most Water  
- 问题简述：给出一个list a,找到一组i,j使得**min(a[i],a[j])\*(j-i)**最大  
  - 思路：设置首位指针h,t 从较小的一段往中间移动，同时更新答案  
  
### 12. Integer to Roman  
- >using this radix:  
>mod = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']<br>
div = [1000,900,500,400,100,90,50,40,10,9,5,4,1]  

### 13. Roman to Integer
- it's same to 12.

### 14. Longest Common Prefix  
- 利用zip(\*strs) 实现行列重排  

### 16. 3Sum Closest
简单的思路如下：
```
class Solution(object):
    def threeSumClosest(self, nums, target):
        res = 0x7fffffff
        nums.sort()
        for i in xrange(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(res - target): res = sum
                if (sum > target):
                    right -= 1
                elif (sum < target):
                    left += 1
                else:
                    return res
        return res
```
复杂度n^2，实际上当target<0时，答案更有可能是两个负数和一个正数，反之答案更有可能是两个正数和一个负数，因此分开处理可以更快的找到最优解。


### 17. Letter Combinations of a Phone Number
 - 用递归的形式会产生一定的迭代开销，故用栈模拟递归的形式提高效率，下面是用栈模拟递归的基本思路：
 ```
        res = [] 
        head = Solution.StackMod(0, '', 0) 
        stack = [head, ] #初始化栈
        while stack: #当栈非空
            head = stack[-1] #获取栈顶元素
            if head.step == length: #递归终点
                res.append(head.now)
                stack.pop() 
            else:
                if head._ < len(diction[digits[head.step]]): #若当前节点还能继续扩展
                    new = Solution.StackMod(head.step + 1, head.now + diction[digits[head.step]][head._])
                    head._ += 1
                    stack.append(new)#新节点入栈
                else:
                    stack.pop() #当前节点出栈
 ```

### 32. Longest Valid Parentheses  
 - 使用stack记录尚未匹配的左括号位置
