from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        high=0
        low=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        res=[]
        while high<=low and left<=right:
            for j in range(left,right+1):
                res.append(matrix[high][j])

            high+=1
            for i in range(high,low+1):
                res.append(matrix[i][right])
                
            right-=1
            if high<=low:
                for j in range(right,left-1,-1):
                    res.append(matrix[low][j])
                low-=1
            if left<=right:
                for i in range(low,high-1,-1):
                    res.append(matrix[i][left])

                left+=1
        return res
matrix = [[2,5,8],
          [4,0,-1]]
s=Solution()
res=s.spiralOrder(matrix)
print(res)