from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen=0
        s=set(nums)
        for i in s:
            if i-1 not in s:
                len=1
                j=i+1
                while j in s:
                    len+=1
                    j+=1
                if len>maxlen:
                    maxlen=len
        return maxlen

S = Solution()
nums = [100,4,200,1,3,2]
print(S.longestConsecutive(nums))
