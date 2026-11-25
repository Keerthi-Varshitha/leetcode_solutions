class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=list(range(1,n+1))
        i=0
        while len(a)>1:
            i=(i+k-1)%len(a)
            a.pop(i)
        return a[0]