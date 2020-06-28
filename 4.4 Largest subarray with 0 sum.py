link:- https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
def maxLen(n, arr):
    d={0:-1}
    m=0
    s=0
    for i in range(n):
        s=s+arr[i]
        if s in d:
            m=max(m,i-d[s])
        else:
            d[s]=i
    return m
