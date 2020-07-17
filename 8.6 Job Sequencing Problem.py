# https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0
t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    arr=[]
    for i in range(0,3*n,3):
        arr.append([l[i],l[i+1],l[i+2]])
        
    arr.sort(reverse=True,key= lambda x:x[2])
    for i in range(n):
        m=max(m,arr[i][1])
    ans=[-1]*m
    s=0
    c=0
    for i in range(n):
        em=arr[i][1]-1
        while em>=0 and ans[em]!=-1:
            em-=1
        if em!= -1:
            ans[em]=arr[i][2]
            s=s+arr[i][2]
            c+=1
        if c==m:
            break
    print(c,s)
