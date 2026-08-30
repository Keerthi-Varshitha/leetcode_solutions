class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                c+=1
                m=max(m,c)
            else:
                c=0
        return m