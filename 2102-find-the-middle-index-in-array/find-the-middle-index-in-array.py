class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum=0
        for num in nums:
            sum+=num
        ls=0
        for i in range(len(nums)):
            rs=sum-ls-nums[i]
            if rs==ls:
                return i
            else:
                ls+=nums[i]
        return -1