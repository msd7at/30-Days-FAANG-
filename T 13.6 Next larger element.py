#https://practice.geeksforgeeks.org/problems/next-larger-element/0
t=int(input())
for q in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    stack=[0]
    ans=[-1]*n
    for i in range(1,n):
        if ar[i]<=ar[stack[-1]]:
            stack.append(i)
        else:
            while len(stack)>0 and ar[i]>ar[stack[-1]] :
                x=stack.pop()
                ans[x]=ar[i]
            stack.append(i)
    print(*ans)
