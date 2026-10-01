class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                a=stack.pop()
                if i==')' and a!='(':
                    return False
                if i==']' and a!='[':
                    return False
                if i=='}' and a!='{':
                    return False
                
        return len(stack)==0