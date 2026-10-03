class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i!='#':
                a.append(i)
            else:
                if a:
                    a.pop()
        for j in t:
            if j!='#':
                b.append(j)
            else:
                if b:
                    b.pop()
        return a==b
