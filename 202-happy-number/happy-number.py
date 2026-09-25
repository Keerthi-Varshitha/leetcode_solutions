class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1:
            if n in a:
                return False
            a.add(n)
            sum=0
            while n>0:
                digit=n%10
                sum+=digit*digit
                n//=10
            n=sum
        return True
