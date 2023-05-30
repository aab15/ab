# MANUAL
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

def findParent(graph, node):
    if graph[node]<0:
        return node
    else:
        temp = findParent(graph, graph[node])
        graph[node] = temp
        return temp

def union(graph, a, b, ans):
    ta = a
    tb = b
    a = findParent(graph, a)
    b = findParent(graph, b)

    if a == b:
        pass
    else:
        ans.append([ta, tb])
        if graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b


inp = sorted(inp, key = lambda inp:inp[2])
graph = [-1]*(N)
answer = []
tot = 0

for u, v, w in inp:
    union(graph, u, v, answer)
    
for item in answer:
    print(item)

for item in answer:
    tot += G[item[0]][item[1]]
    
print(tot)


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