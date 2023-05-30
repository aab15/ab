class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]
    
    def addEdge(self, src, dest):
        self.adj[src].append(dest)

    def DFS(self, start, visited):
        visited[start] = 1
        print(start, end = " ")
        
        for a in self.adj[start]:
            if visited[a] == 0:
                self.DFS(a, visited)

size = int(input("Enter size of Graph: "))
edges = int(input("Enter number of edges: "))

graph = Graph(size)

for i in range(edges):
    src, dest = input("Enter edge between (src dest): ").split()
    src = int(src)
    dest = int(dest)
    graph.addEdge(src, dest)

start = int(input("Enter starting edge: "))
visited = [0]*(size)
graph.DFS(start, visited)