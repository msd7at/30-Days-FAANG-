# link : https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        ed=set("}")
        ed.add(")")
        ed.add("]")
        for i in s:
            if stack==[] and i in ed:
                return False
            else:
                if i in ed:
                    l=stack[-1]
                    if l=="{" and i=="}":
                        stack.pop()
                    if l=="[" and i=="]":
                        stack.pop()
                    if l=="(" and i==")":
                        stack.pop()
                else:
                    stack.append(i)
        if stack==[]:
            return True 
        return False
                    
            
                
                
