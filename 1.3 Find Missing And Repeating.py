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
