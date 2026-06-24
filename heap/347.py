from typing import List

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        heap=[]
        for key,value in count.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for _ , key in heap:
            res.append(key)
        return res
