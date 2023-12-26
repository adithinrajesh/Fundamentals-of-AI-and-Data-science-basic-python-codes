class GreedyBestFirstSearch:
    def __init__(self, nodes, edges, heuristic, adjacency):
        self.nodes = nodes
        self.edges = edges
        self.heuristic = heuristic
        self.adjacency = adjacency
        self.frontier = []
        self.explored = []
        self.path = []

    def greedy_best_first_search(self, initial_node, goal_node):
        self.frontier.append((self.heuristic[initial_node], initial_node))

        while self.frontier:
            self.frontier.sort(key=lambda x: x[0])
            current_node = self.frontier.pop(0)
            self.path.append(current_node[-1])

            if current_node in self.explored:
                continue

            self.explored.append(current_node)

            if current_node[-1] == goal_node:
                print(' -> '.join(self.path))
                return True

            self.frontier = []
            for edge_cost, neighbor in self.adjacency[current_node[-1]]:
                if neighbor not in self.explored:
                    self.frontier.append((self.heuristic[neighbor], neighbor))

        return False

# Example usage:
nodes = ['S', 'A', 'B', 'C', 'D', 'H', 'F', 'G', 'E']
edges = [('S', 'A', 3), ('S', 'B', 2), ('S', 'C', 4), ('B', 'D', 1), ('B', 'H', 3), ('H', 'F', 1), ('H', 'G', 5),
         ('G', 'E', 2)]
heuristic = {'S': 10, 'A': 9, 'B': 7, 'C': 8, 'D': 8, 'H': 6, 'F': 6, 'G': 3, 'E': 0}
adjacency = {
    'S': [(3, 'A'), (2, 'B'), (4, 'C')],
    'A': [],
    'B': [(1, 'D'), (3, 'H')],
    'C': [],
    'D': [],
    'H': [(1, 'F'), (5, 'G')],
    'F': [],
    'G': [(2, 'E')],
    'E': []
}

gbfs = GreedyBestFirstSearch(nodes, edges, heuristic, adjacency)

if gbfs.greedy_best_first_search(nodes[0], nodes[-1]):
    print('Goal reached')
else:
    print("Goal not reached")
