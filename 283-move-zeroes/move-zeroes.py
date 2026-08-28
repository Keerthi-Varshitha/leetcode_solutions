class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[s],nums[i]=nums[i],nums[s]
                s+=1
        return nums