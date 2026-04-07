import heapq

# Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


# Uniform Cost Search Function
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.enqueue((start, [start]), 0)  # (node, path), cost

    visited = set()

    while not pq.is_empty():
        cost, (node, path) = pq.dequeue()

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph.get(node, []):
                if neighbor not in visited:
                    pq.enqueue((neighbor, path + [neighbor]), cost + edge_cost)

    return None


# Graph Definition
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}


# Run UCS
result = uniform_cost_search(graph, 'A', 'G')

# Output
print("Cost and Path:", result)