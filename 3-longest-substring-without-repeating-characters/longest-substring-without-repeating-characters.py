class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        m=0
        for r in range(0,len(s)):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            
            d.add(s[r])
            
            m=max(m,r-l+1)
        return m



             