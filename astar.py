import heapq

# Possible movements: right, left, down, up
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (row, col)
        self.parent = parent      # Parent node for path reconstruction
        self.g = g                # Cost from start node
        self.h = h                # Estimated cost to goal (heuristic)
        self.f = g + h            # Total cost

    def __lt__(self, other):
        return self.f < other.f  # Priority queue comparison

def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """Finds the shortest path from start to goal"""
    rows, cols = len(grid), len(grid[0])
    open_list = []          # Priority queue for nodes to explore
    closed_set = set()      # Set of visited nodes

    # Initialize start node
    start_node = Node(start, None, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)  # Get node with lowest f(n)

        if current.position == goal:  # If goal is reached, reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current.position)

        for move in MOVES:
            neighbor_pos = (
                current.position[0] + move[0],
                current.position[1] + move[1]
            )

            # Check if within grid bounds
            if not (0 <= neighbor_pos[0] < rows and 0 <= neighbor_pos[1] < cols):
                continue

            # Check if position is an obstacle
            if grid[neighbor_pos[0]][neighbor_pos[1]] == "#":
                continue

            # Skip if already visited
            if neighbor_pos in closed_set:
                continue

            # Calculate cost values
            g = current.g + 1                         # Cost to move to neighbor
            h = heuristic(neighbor_pos, goal)         # Heuristic cost (Manhattan)
            neighbor_node = Node(neighbor_pos, current, g, h)
            heapq.heappush(open_list, neighbor_node)  # Add to queue

    return None  # No path found

# 10x15 Grid ('.' = walkable, '#' = obstacle)
grid = [
    list(".#....##......."),
    list("..........#...."),
    list("......##......."),
    list("..............."),
    list("#######..####.."),
    list("..............."),
    list(".....####......"),
    list(".#...#........."),
    list("....#......#..."),
    list("#######..####.."),
    list("...........#..."),
    list(".....####......"),
]

start = (0, 0)       # Start position (top-left corner)
goal = (11, 14)      # Goal position (bottom-right corner)
path = a_star_search(grid, start, goal)

# Print grid with path
if path:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in path:
                print("P", end=" ")  # Mark path
            elif grid[row][col] == "#":
                print("#", end=" ")  # Mark obstacles
            else:
                print(".", end=" ")  # Open space
        print()
else:
    print("No path found!")
