from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        left=intervals[0][0]
        right=intervals[0][1]
        res=[]
        for interval in intervals[1:]:
            if interval[0]>right:
                res.append([left,right])
                left=interval[0]
                right=interval[1]
            else:
                if right<interval[1]:
                    right=interval[1]
        res.append([left,right])
        return res



intervals = [[1,4],[2,3]]
s=Solution()
print(s.merge(intervals))