
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        n= k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,n-1)
        self.reverse(nums,n,len(nums)-1)

    def reverse(self,num,low,high):
        while low<high:
            temp=num[low]
            num[low]=num[high]
            num[high]=temp
            low+=1
            high-=1