from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        ppre=0
        pre=0
        for num in nums:
            cur=max(num+ppre,pre)
            ppre=pre
            pre=cur
        return pre