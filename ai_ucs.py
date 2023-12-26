from queue import PriorityQueue

weighted_graph = {
    'a': [('b', 1), ('c', 4)],
    'b': [('d', 3), ('e', 2)],
    'c': [('f', 5), ('g', 1)],
    'd': [],
    'e': [],
    'f': [],
    'g': []
}

class GraphSearch:
    def __init__(self, weighted_graph):
        self.weighted_graph = weighted_graph

    def uniform_cost_search(self, initial_state, goal_state):
        explored = set()
        frontier = PriorityQueue()
        frontier.put((0, initial_state))

        while not frontier.empty():
            cost, state = frontier.get()

            if state in explored:
                continue

            explored.add(state)
            print(state, end="  ")

            if state == goal_state:
                return True

            for neighbor, edge_cost in self.weighted_graph[state]:
                if neighbor not in explored:
                    total_cost = cost + edge_cost
                    frontier.put((total_cost, neighbor))

        return False

# Example usage:
graph_search = GraphSearch(weighted_graph)
graph_search.uniform_cost_search('a', 'g')
