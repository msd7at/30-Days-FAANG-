# https://leetcode.com/problems/is-graph-bipartite/
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        queue = deque()
        for i in range(len(graph)):
            if i not in color:
                color[i]=0
                queue.append(i)
                while queue:
                    s=queue.popleft()
                    for j in graph[s]:
                        if j  in color:
                            if color[j] == color[s]:
                                return False
                        else:
                            color[j]=1-color[s]
                            queue.append(j)
                            
        return True
                                
                        
