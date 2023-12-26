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

def dfs(graph, current_state, goal_state):
    explored = set()

    def dfs_recursive(node):
        if node not in explored:
            print(node, end=" ")
            explored.add(node)

            if node == goal_state:
                return True

            for adjacent_state in graph[node]:
                if dfs_recursive(adjacent_state):
                    return True

            return False

    dfs_recursive(current_state)

# Example usage:
dfs(graph, 'a', 'c')
