class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr_num=0
        ans=''
        stack=[]
        for i in s:
            if i.isdigit():
                curr_num=curr_num*10+int(i)
            elif i=='[':
                stack.append(curr_num)
                stack.append(ans)
                curr_num=0
                ans=''
            elif i==']':
                ans=stack.pop()+ans*stack.pop()
            else:
                ans+=i
        return ans
