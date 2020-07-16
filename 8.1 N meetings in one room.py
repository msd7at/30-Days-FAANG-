#https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
t=int(input())
for q in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=[]
    for i in range(n):
        ans.append([a[i],b[i],i+1])
    ans.sort(key=lambda x : x[1])
    print(ans[0][2],end=" ")
    prev=ans[0][1]
    for i in range(1,n):
        if ans[i][0]>=prev:
            print(ans[i][2],end=" ")
            prev=ans[i][1]
    print()
