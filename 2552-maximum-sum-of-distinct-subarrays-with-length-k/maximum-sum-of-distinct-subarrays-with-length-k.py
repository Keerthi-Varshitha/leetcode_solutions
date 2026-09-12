class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        window_elements=set()
        s=0
        m=0
        for r in range(len(nums)):
            while nums[r] in window_elements:
                window_elements.remove(nums[l])
                s-=nums[l]
                l+=1
            window_elements.add(nums[r])
            s+=nums[r]
            if (r-l+1)==k:
                m=max(m,s)
                window_elements.remove(nums[l])
                s-=nums[l]
                l+=1
        return m