#link: https://www.geeksforgeeks.org/counting-inversions/

import sys
sys.setrecursionlimit(1000000000)
def mergesort(arr,n):
    ta=[0]*n
    return _mergesort(arr,ta,0,n-1)

def _mergesort(arr,ta,l,r):
    ic=0
    if l<r:
        m=(l+r)//2
        ic= ic+ _mergesort(arr,ta,l,m)
        ic= ic+ _mergesort(arr,ta,m+1,r)
        ic= ic+merge(arr,ta,l,m,r)
    return ic
    
def merge(ar,ta,l,m,r):
    i=l
    j=m+1
    k=l
    ic=0
    while i <=m and j<=r:
        if ar[i]<=ar[j]:
            ta[k]=ar[i]
            i+=1
            k+=1
        else:
            ta[k]=ar[j]
            ic=ic+(m-i+1)
            j+=1
            k+=1
    while i<=m:
        ta[k]=ar[i]
        i+=1
        k+=1
    while j<=r:
        ta[k]=ar[j]
        j+=1
        k+=1
    for x in range(l,r+1):
        ar[x]=ta[x]
    return ic 
        
t=int(input())
for q in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=mergesort(arr,n)
    print(ans)
