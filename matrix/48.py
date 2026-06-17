from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=n//2-1
        for i in range(m+1):
            for j in range(n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[n-1-i][j]
                matrix[n-1-i][j]=temp
        for i in range(n):
            for j in range(i,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s=Solution()
s.rotate(matrix)
print(matrix)