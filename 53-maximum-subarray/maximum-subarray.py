class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0#[-1,-1,-1,-1,5]
        m=nums[0]
        for i in range(0,len(nums)):
            s+=nums[i]
            
            if s>m:
                m=s
            if s<0:
                s=0
        return m