# correct ans but not accepting   # hackerearth ki mkb
#link  :  https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/nearest-smaller-element-929558b4/description/
n=int(input())
arr=list(map(int,input().split()))
s = list() 
top=-1
g=[]
for i in range(n):
    while(len(s)>0 and s[top]>=arr[i]):
        s.pop()
    if(len(s)==0):
        g.append(-1)
    else:
        g.append(s[top])
    s.append(arr[i])
print(' '.join(str(i) for i in g))
