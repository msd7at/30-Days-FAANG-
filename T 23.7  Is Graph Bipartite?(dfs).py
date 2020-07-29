# link: https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j]==color[i]:
                        return False
                else:
                    color[j]=1-color[i]
                    if dfs(j)==False:
                        return False
            return True
                        
            
        color={}
        for i in range(len(graph)):
            if i not in color:
                color[i] =0
                if dfs(i)==False:
                    return False
        return True
