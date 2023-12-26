def alpha_beta_search(graph, current_node, alpha, beta, is_maximizing_player, pruning_count):
    if str(current_node).isnumeric():
        return int(current_node), alpha if is_maximizing_player else beta
    
    best_value = float("-inf") if is_maximizing_player else float("inf")
    
    for child_node in graph[current_node]:
        child_value, updated_alpha = alpha_beta_search(graph, child_node, alpha, beta, not is_maximizing_player, pruning_count)
        
        if is_maximizing_player:
            best_value = max(best_value, child_value)
            alpha = max(best_value, alpha)
            
        else:
            best_value = min(best_value, child_value)
            beta = min(best_value, beta)
            
        if alpha >= beta:
            pruning_count[0] += 1
            break
            
    return best_value, alpha if is_maximizing_player else beta

graph = {
    'a': ['b', 'c', 'd'],
    'b': ['f', 'e'],
    'c': ['h', 'g'],
    'd': ['i'],
    'e': ['j', 'k'],
    'f': ['l', 'm'],
    'g': ['n'],
    'h': ['o', 'p'],
    'i': ['q'],
    'j': [10, 20],
    'k': [30, 40],
    'l': [50, 12],
    'm': [8, 10],
    'n': [14, 18],
    'o': [9, 25],
    'p': [23, 29],
    'q': [40, 45]
}

# Initialize the pruning count
pruning_count = [0]

best_value, alpha = alpha_beta_search(graph, 'a', float("-inf"), float("inf"), True, pruning_count)
print("Best value =", best_value)
print("Alpha =", alpha)
print("Pruning Count =", pruning_count[0])
