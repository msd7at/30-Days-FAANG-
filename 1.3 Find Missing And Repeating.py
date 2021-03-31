link:-https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0
TC:-O(n)
t=int(input())
for q in range(t):
    n=int(input())
    l = input().split()
    for i in range(n):
        l[i] = int(l[i])
    su=n*(n+1)
    su=su//2
    s=sum(l)
    x=0
    for i in range(n):
        if l[abs(l[i])-1]>0:
            l[abs(l[i])-1] = -l[abs(l[i])-1]
        else:
            x=abs(l[i])
    f=abs(s-x)
    print(x,su-f)
    
    # approach 2
    class Solution:
        
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        l=len(A)
        newArray=[0]*(l+1)
        for i in A:
            newArray[i]+=1
        ans=[0,0]
        for i in range(1,l+1):
            if newArray[i] == 0 :
                ans[1]=i
            elif newArray[i]>1:
                ans[0]=i
        return ans
            
        
