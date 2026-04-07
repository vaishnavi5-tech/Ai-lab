# Depth First Search with User Input

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            # reverse to maintain input order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None


# -------- USER INPUT --------
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# -------- RUN DFS --------
result = dfs(graph, start, goal)

# -------- OUTPUT --------
if result:
    print("Path found:", result)
else:
    print("No path found")