  
# https://www.youtube.com/watch?v=oNI0rf2P9gE
'''Complexity
Worst case time complexity: Θ(n^3)
Average case time complexity: Θ(n^3)
Best case time complexity: Θ(n^3)
'''
n=int(input())
orig=[]
for i in range(n):
    for j in range(1):
        temp=[int(s) for s in input().split()]
        orig.append(temp)
#Floyd-Warshall Algorithm: Shortest path 
for k in range(n):
    for i in range(n):
        for j in range(n):
            orig[i][j]=min(orig[i][j],orig[i][k]+orig[k][j])
print(orig)
