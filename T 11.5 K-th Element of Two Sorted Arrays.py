t=int(input())
for q in range(t):
    l1,l2,k=map(int,input().split())
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    i,j=0,0
    an=0
    while i<l1 or j<l2:
        if i==l1:
            an+=1
            if an==k:
                print(nums2[j])
            j+=1
        elif j==l2:
            an+=1
            if an==k:
                print(nums1[i])
            i+=1
        elif nums1[i]<nums2[j]:
            an+=1
            if an==k:
                print(nums1[i])
            i+=1
            
        else:
            an+=1
            if an==k:
                print(nums2[j])
            j+=1
            
        
