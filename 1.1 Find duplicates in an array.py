#Question link:
#GFG:-https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
#o(n) and O(1) space
l=len(a)
for i in range(l):
	a[a[i]%l]+=l
for i in range(l):
	if a[i]>=(l**2):
		print(a[i])
#sol 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using hashmap
        # by sorting and then find
        t=h=nums[0]
        
        while True:
            t=nums[t]
            h=nums[nums[h]]
            if t==h:
                break
        t=nums[0]
        while t!=h:
            t=nums[t]
            h=nums[h]
        return h
    
		
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
