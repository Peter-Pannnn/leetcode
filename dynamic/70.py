class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        num=[0]*n
        num[0]=1
        num[1]=2
        for i in range(2,n):
            num[i]=num[i-1]+num[i-2]
        return num[n-1]