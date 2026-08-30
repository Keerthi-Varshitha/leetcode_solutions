class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        c=3
        if n<=3:
            return n
        for i in range(4,n+1):
            a=b
            b=c
            c=a+b
        return c