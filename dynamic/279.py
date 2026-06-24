class Solution:
    def numSquares(self, n: int) -> int:
        df=[9999999]*(n+1)
        df[0]=0
        for num in range(1,n+1):
            j=1
            while j*j<=num:
                sq=j*j
                df[num]=min(df[num],df[num-sq]+1)
                j+=1
        return df[n]