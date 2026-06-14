class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=-1
        max_len=0
        sub_str=""
        while j<len(s)-1:

            if s[j+1] in sub_str:
                i=sub_str.index(s[j+1])+i+1
                j+=1
            else:
                j+=1
            sub_str=s[i:j+1]
            max_len=max(max_len,len(sub_str))
        return max_len

    def lengthOfLongestSubstringOptimal(self, s: str) -> int:
        last_index = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_index and last_index[char] >= left:
                left = last_index[char] + 1

            last_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstringOptimal("abcabcbb"))
