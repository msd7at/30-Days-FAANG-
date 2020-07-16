#  https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
t=int(input())
for q in range(t):
    v,n=map(int,input().split())
    co=list(map(int,input().split()))
    co.sort()
    l=len(co)-1
    c=0
    while l>=0 and v>0:
        if v-co[l]<0:
            l-=1
        if v>=co[l]:
            c+=1
            v-=co[l]
        else:
            l-=1
     
    if v==0 :
        print(c)
    else:
        print(-1)
        print(c,v)
