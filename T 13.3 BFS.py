import collections
def bfs(g,root):
  visited=set()
  queue=collections.dequeue([root])
  visited.add(root)
  while queue:
    s=queue.popleft()
    for i in g[s]:
      if i not in visited:
        visited.add(i)
        queue.append(i)
