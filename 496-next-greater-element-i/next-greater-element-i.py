class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        for i in nums1:
            a=-1
            target_found=False
            for j in nums2:
                if i==j:
                    target_found=True
                if target_found and j>i:
                    a=j
                    break
            stack.append(a)
        return stack
                    