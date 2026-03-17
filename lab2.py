class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    data = input("Enter node value (-1 for no node): ")
    
    if data == "-1":
        return None
    
    node = Node(int(data))
    
    print(f"Enter left child of {data}")
    node.left = build_tree()
    
    print(f"Enter right child of {data}")
    node.right = build_tree()
    
    return node


from collections import deque

def bfs(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Build tree from user input
root = build_tree()

print("BFS Traversal:")
bfs(root)