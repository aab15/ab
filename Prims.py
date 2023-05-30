N = int(input("Enter the size of the graph: "))
edges = int(input("Enter number of edges: "))
G = [[0] * N for _ in range(N)]

for i in range(edges):
    src, dest, weight = input("Enter src, dest, weight: ").split()
    G[int(src)][int(dest)] = int(weight)
# ----------------------------------------------------------------------

visited = [0]*N
no_edge = 0
tot_cost = 0

visited[0] = True

print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = float('inf')
    a = 0
    b = 0
    for m in range(N):
        if visited[m]:
            for n in range(N):
                if ((not visited[n]) and G[m][n]): 
                    if G[m][n] < minimum:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    visited[b] = True
    no_edge += 1
    tot_cost += G[a][b]

print(f'Min Cost: {tot_cost}')

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