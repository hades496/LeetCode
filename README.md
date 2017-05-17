# LeetCode  
- My LeetCode solution  
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
### 14. Longest Common Prefix  
- 利用zip(\*strs) 实现行列重排  
