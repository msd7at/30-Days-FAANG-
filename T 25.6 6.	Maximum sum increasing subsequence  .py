# link:  https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
t=int(input())
for q in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    ar=[]
    for i in range(n):
        ar.append(nums[i])
    m=0
    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j] and ar[i]< ar[j]+nums[i]:
                ar[i]=ar[j]+nums[i]
            
    m=max(ar)
    print(m)
