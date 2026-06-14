from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0

    

s=Solution()
s.moveZeroes([1,2,0,5,0])