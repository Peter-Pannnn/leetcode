from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count=[0]*26
        win=[0]*26
        res=[]
        for i in p:
            p_count[ord(i)-ord('a')]+=1
        
        left=0
        for right in range(len(s)):
            win[ord(s[right])-ord('a')]+=1
            if right-left>len(p)-1:
                win[ord(s[left])-ord('a')]-=1
                left+=1
            if right-left==len(p)-1:
                if win==p_count:
                    res.append(left)



        return res
    



