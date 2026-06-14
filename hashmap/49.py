from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            a = "".join(sorted(s))
            if a in hashmap:
                l = hashmap[a]
                l.append(s)
                hashmap[a] = l
            else:
                hashmap[a] = [s]
        return list(hashmap.values())



test = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(test))