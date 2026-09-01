class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible=[]
        non_divisible=[]
        for i in range(1,n+1):
            if i%m==0:
                divisible.append(i)
            else:
                non_divisible.append(i)
        return sum(non_divisible)-sum(divisible)