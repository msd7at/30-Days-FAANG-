# https://www.youtube.com/watch?v=_QPrHo88mAc
def printmaze(soln,n):
    for i in soln:
        print(i)
    print()
def helpmaze(arr,n,soln,x,y):
    if x==n-1 and y==n-1 :
        soln[x][y]=1
        printmaze(soln,n)
        return True
    if x<0 or x>n-1 or y<0 or y>n-1 or arr[x][y]==0 or soln[x][y]==1:
        return 
    soln[x][y]=1
    helpmaze(arr,n,soln,x-1,y)
    helpmaze(arr,n,soln,x+1,y)
    helpmaze(arr,n,soln,x,y-1)
    helpmaze(arr,n,soln,x,y+1)
    soln[x][y]=0
    
def findPath(arr, n):
    soln=[]
    for i in range(n):
        soln.append([0]*n)
    helpmaze(arr,n,soln,0,0)

arr=[]
n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    arr.append(x)
findPath(arr,n)
    
    
    
    
    
    
    
    
    
    
