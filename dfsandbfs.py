from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  
    
    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(node)
        print(node, end=' ')
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Input Handling
g = Graph()
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_node = int(input("Enter start node for traversal: "))

print("DFS (Recursive):")
g.dfs_recursive(start_node)

print("\nBFS:")
g.bfs(start_node)
