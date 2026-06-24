from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        map=[[0 for _ in range(n) ]for _ in range(m)]

        for i in range(m):
            for j in range(n):
                h=map[i-1][j] if i-1>=0 else float("inf")
                l=map[i][j-1] if j-1 >=0 else float("inf")
                if h==float("inf") and l==float("inf"):
                    map[i][j]=grid[i][j]
                    continue
                map[i][j]=min(grid[i][j]+h,grid[i][j]+l)

        return map[m-1][n-1]
