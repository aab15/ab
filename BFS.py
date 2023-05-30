from collections import deque
 
class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def addEdge(self, src, dest):
        self.adj[src].append(dest)

    def recursiveBFS(self, q, discovered):
        if not q:
            return
        v = q.popleft()
        print(v, end=' ')
        for u in graph.adj[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)
        self.recursiveBFS(graph, q, discovered)


size = int(input("Enter size of Graph: "))
edges = int(input("Enter number of edges: "))

graph = Graph(size)

for i in range(edges):
    src, dest = input("Enter edge between (src dest): ").split()
    src = int(src)
    dest = int(dest)
    graph.addEdge(src, dest)


visited = [0]*(size)
q = deque()

start = int(input("Enter starting edge: "))

visited[start] = True
q.append(start)

graph.recursiveBFS(q, visited)