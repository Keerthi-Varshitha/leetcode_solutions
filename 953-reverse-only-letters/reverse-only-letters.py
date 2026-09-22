class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        cur=''
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                cur+=s[i]
        res=''
        i=0
        for ch in s:
            if not ch.isalpha():
                res+=ch
            else:
                res+=cur[i]
                i+=1
        return res
