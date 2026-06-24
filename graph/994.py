from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        fresh=0
        t=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        while q:
            if not fresh == 0:
                t+=1
            size=len(q)
            for _ in range(size):
                pi,pj=q.popleft()
                if pi-1>=0:
                    if grid[pi-1][pj]==1:
                        grid[pi-1][pj]=2
                        fresh-=1
                        q.append((pi-1,pj))
                if pi+1<=m-1:
                    if grid[pi+1][pj]==1:
                        grid[pi+1][pj]=2
                        fresh-=1
                        q.append((pi+1,pj))
                if pj-1>=0:
                    if grid[pi][pj-1]==1:
                        grid[pi][pj-1]=2
                        fresh-=1
                        q.append((pi,pj-1))
                if pj+1<=n-1:
                    if grid[pi][pj+1]==1:
                        grid[pi][pj+1]=2
                        fresh-=1
                        q.append((pi,pj+1))
        if fresh==0:
            return t
        else:
            return -1
