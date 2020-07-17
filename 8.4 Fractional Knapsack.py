https://practice.geeksforgeeks.org/problems/fractional-knapsack/0#link: https://practice.geeksforgeeks.org/problems/fractional-knapsack/0
t=int(input())
for q in range(t):
    n,w=map(int,input().split())
    l=list(map(int,input().split()))
    pf=[]
    for i in range(0,2*n,2):
        X=l[i]/l[i+1]
        pf.append([X,i])
    pf.sort(reverse=True)
    ans=0
    for i in range(n):
        x=pf[i][1]
        temp=l[x+1]
        if w - temp>0:
            w-=temp
            ans=ans+ l[pf[i][1]]
        elif w - temp==0:
            w-=temp
            ans=ans+ l[pf[i][1]]
            break
        else:
            ans=ans+((w/temp)*l[pf[i][1]])
            break
    print(round(ans,2))
