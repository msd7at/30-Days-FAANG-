#Question link:
#GFG:-https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
#O(n)space and Time Solution

def duplicates(arr, n): 
	d=[0]*n
	l=[]
	p=0
	for i in arr:
	    d[i]+=1
	    if d[i]==2:
	        p=8
	if p==0:
	    return [-1]
	else:
	    for i in range(n):
	        if d[i]>1:
	            l.append(i)
	    return l
