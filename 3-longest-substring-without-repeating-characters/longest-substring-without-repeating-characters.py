class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        l=0
        m=0
        for r in range(0,len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.append(s[r])
            m=max(m,r-l+1)
        return m
