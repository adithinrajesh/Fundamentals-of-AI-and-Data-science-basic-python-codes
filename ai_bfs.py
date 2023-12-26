from collections import deque

graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': [],
    'e': ['h', 'i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []
}

def bfs(graph, initial_state, goal_state):
    explored = set()
    frontier = deque([initial_state])

    while frontier:
        current_state = frontier.popleft()

        if current_state == goal_state:
            print_path(initial_state, goal_state)
            return

        if current_state not in explored:
            print(current_state, end=" ")
            explored.add(current_state)

            for adjacent_state in graph[current_state]:
                if adjacent_state not in explored and adjacent_state not in frontier:
                    frontier.append(adjacent_state)

def print_path(initial_state, goal_state):
    print("\nPath from {} to {}:".format(initial_state, goal_state))
    print(f"{initial_state} -> {goal_state}")

# Example usage:
bfs(graph, 'a', 'd')
