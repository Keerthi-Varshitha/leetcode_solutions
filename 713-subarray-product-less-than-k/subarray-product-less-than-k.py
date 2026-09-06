class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        r=0
        p=1
        c=0
        while r<=len(nums)-1:
            p*=nums[r]
            
            while p>=k and l<=r:
                p//=nums[l]
                l+=1
            c+=(r-l+1)
            r+=1
        return c


