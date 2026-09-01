class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            v=str(i)
            if '0' in v:
                continue
            for j in v:
                if i%int(j)!=0:
                    break
            else:
                res.append(i)
        return res