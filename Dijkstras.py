N = int(input("Enter Size of Graph: "))
edges = int(input("Enter number of edges: "))
inp = []

G = [[0]*N for _ in range(N)]

for i in range(edges):
    edge = []
    src, dest, weight = input("Enter src, dest, weight: ").split()
    edge.append(int(src))
    edge.append(int(dest))
    edge.append(int(weight))
    inp.append(edge)
    G[int(src)][int(dest)] = int(weight)
# ---------------------------------------------------------------------------------
from heapq import *

def dijkstra(graph, start, visited, distance):
    distance[start] = 0
    bag = []
    heappush(bag, [0, start])

    while(bag):
        d, node = heappop(bag)
        visited[node] = 1
        for currdis, nextnode in graph[node]:
            if not visited[nextnode] and currdis+distance[node] < distance[nextnode]:
                distance[nextnode] = currdis+distance[node]          
                heappush(bag, [distance[node]+currdis, nextnode])      
    
    print(f'Start = {start}')
    print("Dest    Cost")
    for node, dis in distance.items():
        print(f'{node}    ->    {dis}')

# ---------------------------------------------------------------------------------

visited = {}
graph = {}
distance = {}

for i in range(N):
    graph[i] = []
    visited[i] = 0
    distance[i] = float('inf')

for u, v, w in inp:
    graph[u].append([w, v])
    graph[v].append([w, u])

start = int(input("Enter starting vertex: "))
dijkstra(graph, start, visited, distance)

# # Input
# 5
# 16
# 0 1 2
# 0 3 6
# 1 0 2
# 1 2 3
# 1 3 8
# 1 4 5
# 2 1 3
# 2 4 7
# 3 0 6
# 3 1 8
# 3 4 9
# 4 1 5
# 4 2 7
# 4 3 9 
# 1
