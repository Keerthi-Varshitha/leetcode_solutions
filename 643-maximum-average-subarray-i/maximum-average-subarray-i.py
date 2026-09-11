class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k-1
        m=float('-inf')# if we ant max then float('inf')
        s=0
        for i in range(l,r+1):
            s+=nums[i]
        m=s/k
        while r<len(nums)-1:
            s-=nums[l]
            l+=1
            r+=1
            s+=nums[r]
            m=max(m,s/k)
        return m