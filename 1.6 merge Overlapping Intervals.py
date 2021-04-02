
#leetcode
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        for i in intervals:
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1]=max(ans[-1][1],i[1])
        return ans
    
    
#link : = https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
t=int(input())
for q in range(t):
    n=int(input())
    ar=[]
    ti=[int(b) for b in input().split()]
    for i in range(n):
        jk=[]
        jk.append(ti[2*i])
        jk.append(ti[2*i+1])
        ar.append(jk)
    ar.sort()
    m=[]
    s=-10000
    max= -10000
    for i in range(n):
        a=ar[i]
        if a[0]>max:
            if i!=0 :
                m.append([s,max])
            max=a[1]
            s=a[0]
        else:
            if a[1]>=max:
                max=a[1]
    if max!= -10000 and [s,max] not in m:
        m.append([s,max])
    for i in m:
        print(i[0],i[1],end=" ")
    print()
