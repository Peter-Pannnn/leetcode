from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        i=0
        j=len(height)-1
        while j-i!=0:
            s=min(height[i],height[j])*(j-i)
            if s>max:
                max=s
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))