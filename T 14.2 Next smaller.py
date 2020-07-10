# next smallest right side
"""
def rightSmaller( arr):
        n=len(arr)
        s = list() 
        top=-1
        g=[]
        for i in range(n-1,-1,-1):
            while(len(s)>0 and s[top]>=arr[i]):
                s.pop()
            if(len(s)==0):
                g.append(-1)
            else:
                g.append(s[top])
            s.append(arr[i])
        
        return g[::-1]  
n=int(input())
ar=list(map(int,input().split()))
print(rightSmaller(ar))


"""
# next smallest right side
n=int(input())
ar=list(map(int,input().split()))
stack=[0]
ans=[-1] *n
for i in range(1,n):
  while stack and ar[stack[-1]]>=ar[i]:
    x=stack.pop()
    ans[x]=ar[i]
  stack.append(i)
print(*ans)
