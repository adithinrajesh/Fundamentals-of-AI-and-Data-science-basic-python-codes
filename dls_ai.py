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

def dls(graph, current_state, goal_state, depth_limit, current_depth):
    if current_depth > depth_limit:
        return False

    print(current_state, end=" ")

    if current_state == goal_state:
        return True

    for adjacent_state in graph[current_state]:
        if dls(graph, adjacent_state, goal_state, depth_limit, current_depth + 1):
            return True

    return False

def depth_limited_search(graph, initial_state, goal_state, depth_limit):
    print("Depth Limited Search:")
    explored = set()
    if not dls(graph, initial_state, goal_state, depth_limit, 0):
        print("\nGoal state not found.")

# Example usage:
depth_limited_search(graph, 'a', 'd', 3)
