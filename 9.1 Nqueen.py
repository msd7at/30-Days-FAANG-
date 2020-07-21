# https://practice.geeksforgeeks.org/problems/n-queen-problem/0
# vid  https://www.youtube.com/watch?v=jFwREev_yvU&t=928s
def solvequeen(boa,n,row,ans):
    if row==n:
        for  i in range(n):
            for j in range(n):
                if boa[i][j]==1:
                    ans.append(j+1)
                    break
    for pos in range(n):
        if safe(boa,row,pos,n):
            boa[row][pos]=1
            nextqueen=solvequeen(boa,n,row+1,ans)
            if nextqueen:
                return True
            boa[row][pos]="."
    return False
def safe(boa,row,col,n):
    for i in range(n):
        if boa[i][col]==1:
            return False
    i=row
    j=col
    while i>=0 and j>=0:
        if boa[i][j]==1:
            return False
        i-=1
        j-=1
        
    i=row
    j=col
    while i>=0 and j<n:
        if boa[i][j]==1:
            return False
        i-=1
        j+=1
    return True
    
t=int(input())
for q in range(t):
    n=int(input())
    if n==1:
        print("[1 ]")
    elif n==3 or n==2:
        print("-1")
    else:
        boa=[['.'] * n for _ in range(n)]
        ans=[]
        solvequeen(boa,n,0,ans)
        for i in range(0,len(ans),n):
            kk="["
            for j in range(i,i+n):
                if i==j:
                    kk+=str(ans[j])
                elif j==i+n-1:
                    kk=kk+" "+str(ans[j])+" ]"
                
                else:
                    kk+=" "+str(ans[j])
            print(kk,end=" ")
            
                
        print()
