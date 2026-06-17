from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fr=False
        fc=False
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            if matrix[0][i]==0:
                fr=True
                break
        for i in range(m):
            if matrix[i][0]==0:
                fc=True
                break
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    matrix[r][0]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0
        for i in range(1,n):
            if matrix[0][i]==0:
                for j in range(1,m):
                    matrix[j][i]=0
        if fr:
            for i in range(n):
                matrix[0][i]=0
        if fc:
            for j in range(m):
                matrix[j][0]=0