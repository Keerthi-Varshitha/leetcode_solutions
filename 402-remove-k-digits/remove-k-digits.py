class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num)==k:
            return '0'
        stack=[]
        for i in num:
            while stack and i<stack[-1] and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack=stack[:-k]
        res=''.join(stack).lstrip("0")
        return res if res else '0'
