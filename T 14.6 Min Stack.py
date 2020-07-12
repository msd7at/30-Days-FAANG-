# link :  https://leetcode.com/problems/min-stack/
# explanation : https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x < self.min[-1]:
                self.min.append(x)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(x)
            
    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
