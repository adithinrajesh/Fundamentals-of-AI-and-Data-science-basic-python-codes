from collections import deque

class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def depth_limited_search(self, start, goal, depth_limit):
        frontier = deque([(start, [start])])
        explored = set()

        while frontier:
            current_state, path = frontier.pop()

            if current_state == goal:
                return True, path

            if len(path) <= depth_limit:
                explored.add(current_state)

                for neighbor in self.graph[current_state]:
                    if neighbor not in explored:
                        frontier.append((neighbor, path + [neighbor]))

        return False, []

    def iterative_deepening_search(self, start, goal, max_depth):
        print("Iterative Deepening Search:")
        for depth_limit in range(max_depth + 1):
            found, path = self.depth_limited_search(start, goal, depth_limit)
            if found:
                print(f"Goal state found at depth limit {depth_limit}. Path: {path}")
                return

# Example usage:
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

search = GraphSearch(graph)
search.iterative_deepening_search('a', 'g', 5)
