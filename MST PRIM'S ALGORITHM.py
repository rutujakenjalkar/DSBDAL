import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)

    # Build adjacency list
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        # Only add edge to MST if it's not the starting node
        if parent != -1:
            mst_edges.append((parent, u, weight))

        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))  # u is parent of v

    return mst_edges, total_cost

# ========== Dynamic Input ==========
edges = []
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

print("\nEnter each edge in the format: u v weight (0-indexed nodes)")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Print all input edges
print("\nAll Edges:")
for u, v, w in edges:
    print(f"{u} - {v} with weight {w}")

# Run Prim's algorithm
mst, cost = prim(n, edges)

# Print MST result
print("\nEdges in Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} with weight {w}")
print("\nTotal cost of MST:", cost)
