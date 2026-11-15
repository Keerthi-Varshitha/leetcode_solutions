class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        n=len(nums)
        a=[-1]*n
        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]:
                a[stack.pop()]=nums[i%n]
            if i<n:
                stack.append(i)
        return a
            