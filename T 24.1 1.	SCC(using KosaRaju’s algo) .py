#link:  https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
#video : https://www.youtube.com/watch?v=32Ll35mhWg0&t=407s
def dfs(g,src,finTime,vis):
    vis[src]=1
    for neigh in g[src]:
        if not vis[neigh]:
            dfs(g,neigh,finTime,vis)
    finTime+=[src]
 
def countSCCs(g,v):
    finTime=[]
    vis=[0]*v
    for i in range(v):
        if not vis[i]:
            dfs(g,i,finTime,vis)
    tg=defaultdict(list)
    for node in range(v):
        for neigh in g[node]:
            tg[neigh]+=[node]
    scc=0
    vis=[0]*v
    while finTime:
        cur=finTime.pop()
        if not vis[cur]:
            scc+=1
            dfs(tg,cur,[],vis)
    return scc

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print (countSCCs(graph, n))
        
# Contributed By: Pranay Bansal
# } Driver Code Ends
