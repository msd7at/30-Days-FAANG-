# link: https://practice.geeksforgeeks.org/problems/minimum-platforms/0
def findPlatform(arr,dep,n):
    arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
   
    while (i < n and j < n): 
     
        if (arr[i] <=dep[j]): 
          
            plat_needed+=1
            i+=1
   
              
            if (plat_needed > result):  
                result = plat_needed 
          
        else: 
          
            plat_needed-=1
            j+=1
          
    return result 
t=int(input())
for q in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(findPlatform(a,b,n))
