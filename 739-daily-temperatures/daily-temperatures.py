class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                index=stack.pop()
                ans[index]=i-index
            stack.append(i)
        return ans