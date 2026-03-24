def iterative_dfs(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == target:
                print("\nTarget found!")
                return

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("\nTarget not found")


# -------- USER INPUT --------

graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ").strip()
    
    neighbors_input = input(f"Enter neighbors of {node} (space separated): ").strip()
    
    if neighbors_input == "":
        graph[node] = []
    else:
        graph[node] = neighbors_input.split()

start = input("Enter starting node: ").strip()
target = input("Enter target node: ").strip()

print("\nDFS Traversal:")
iterative_dfs(graph, start, target)