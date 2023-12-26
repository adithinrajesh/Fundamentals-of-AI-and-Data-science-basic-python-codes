def is_safe(node, color, assignment, graph):
    """
    Check if assigning a color to a node is safe based on the current assignment and graph constraints.

    Parameters:
    - node: The current node to check.
    - color: The color to be assigned to the node.
    - assignment: The current assignment of colors to nodes.
    - graph: The graph representation.

    Returns:
    - True if the assignment is safe, False otherwise.
    """
    return all(assignment.get(neighbour) != color for neighbour in graph[node])

def backtrack(graph, colors):
    """
    Backtracking algorithm for graph coloring.

    Parameters:
    - graph: The graph representation.
    - colors: The list of available colors.

    Returns:
    - A valid color assignment for each node, or None if no solution exists.
    """
    def rec_backtrack(node_index):
        if node_index == len(graph):
            return True
        node = list(graph.keys())[node_index]
        for color in colors:
            if is_safe(node, color, assignment, graph):
                assignment[node] = color
                if rec_backtrack(node_index + 1):
                    return True
                assignment[node] = None
        return False

    assignment = {node: None for node in graph}
    if rec_backtrack(0):
        return assignment
    return None

graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'b', 'e'],
    'e': ['b', 'c', 'd']
}
colors = ['Red', 'Green', 'Blue']
solution = backtrack(graph, colors)

if solution:
    for node, color in solution.items():
        print("Node =", node, "Color =", color)
else:
    print("No solution exists")
