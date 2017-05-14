class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        ans = min(height[l],height[r])*(r-l)
        while (True):
            print 'l=%d r=%d'%(l,r)
            if (height[l]<height[r]):
                i=l
                while (height[i]<=height[l] and i<r) : i+=1
                if l<i and i<r :l=i
                else : break
            else:
                i=r
                while (height[i]<=height[r] and l<i) : i-=1
                if l<i and i<r :r=i
                else: break
            temp = min(height[l],height[r])*(r-l)
            if (temp>ans):
                ans=temp
        return (ans)
