class AStarSearch:
    def __init__(self, graph, h_value):
        self.graph = graph
        self.h_value = h_value
        self.closed_list = []
        self.g = {}

    def a_star_search(self, start, goal):
        open_list = [(0, start)]
        self.g[start] = 0

        while open_list:
            open_list.sort()
            open_list.reverse()
            f_value, state = open_list.pop(0)
            print(state, end=" ")

            if state not in self.closed_list:
                self.closed_list.append(state)
                if state == goal:
                    return True

            for neighbor, weight in self.graph[state]:
                g_value = weight + self.g[state]
                if neighbor not in self.g or g_value < self.g[neighbor]:
                    self.g[neighbor] = g_value
                    open_list.append((g_value + self.h_value[neighbor], neighbor))

        return False

# Example usage:
graph = {'S': [('A', 3), ('D', 4)],
         'A': [('B', 4), ('D', 5)],
         'B': [('C', 4), ('E', 5)],
         'C': [],
         'D': [('E', 2)],
         'E': [('F', 4)],
         'F': [('G', 3.5)],
         'G': []}
h_value = {'S': 11.5, 'A': 10.1, 'B': 5.8, 'C': 3.4, 'D': 9.2, 'E': 7.1, 'F': 3.5, 'G': 0}

astar_search = AStarSearch(graph, h_value)

if astar_search.a_star_search('S', 'G'):
    print('\nGoal reached')
else:
    print("\nGoal not reached")
