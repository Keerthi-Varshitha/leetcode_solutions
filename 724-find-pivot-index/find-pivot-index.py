class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum=0
        for num in nums:
            sum+=num
        ls=0
        for i in range(len(nums)):
            rs=sum-ls-nums[i]
            if ls==rs:
                return i
            ls+=nums[i]
        return -1