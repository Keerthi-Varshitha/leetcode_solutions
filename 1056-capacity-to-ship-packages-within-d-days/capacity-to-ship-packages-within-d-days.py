class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            capacity=mid
            used_days=1
            current_weight=0
            for i in weights:
                if current_weight+i>capacity:
                    used_days+=1
                    current_weight=i
                else:
                    current_weight+=i
            if used_days<=days:
                r=mid
            else:
                l=mid+1
        return l