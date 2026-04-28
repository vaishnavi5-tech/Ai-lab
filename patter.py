import heapq

# Goal State
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# ----------- Puzzle Class -----------
class Puzzle:
    def __init__(self, state, parent=None, move="", g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # Cost so far
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        # Manhattan Distance
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = [
            ("Up", x-1, y),
            ("Down", x+1, y),
            ("Left", x, y-1),
            ("Right", x, y+1)
        ]

        for move_name, new_x, new_y in moves:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                successors.append(Puzzle(new_state, self, move_name, self.g + 1))

        return successors

    def __lt__(self, other):
        return self.f < other.f


# ----------- A* Algorithm -----------
def astar(initial_state):
    start = Puzzle(initial_state)
    open_list = []
    heapq.heappush(open_list, start)

    visited = set()

    while open_list:
        current = heapq.heappop(open_list)

        # Convert state to tuple for visited check
        state_tuple = tuple(tuple(row) for row in current.state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current.is_goal():
            return current

        for successor in current.generate_successors():
            heapq.heappush(open_list, successor)

    return None


# ----------- Print Solution -----------
def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        print(f"Step {i}: Move {step.move}")
        for row in step.state:
            print(row)
        print()


# ----------- MAIN -----------
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = astar(initial_state)

if solution:
    print_solution(solution)
else:
    print("No solution found")