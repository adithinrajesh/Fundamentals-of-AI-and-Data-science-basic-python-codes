import random

def mutate(board1, board2):
    # Swap a random position between two boards
    b1 = list(board1)
    b2 = list(board2)
    x = random.randint(0, 7)
    b1[x], b2[x] = b2[x], b1[x]
    
    # Mutate a random position in each board
    b1[random.randint(0, 7)] = str(random.randint(1, 8))
    b2[random.randint(0, 7)] = str(random.randint(1, 8))
    
    return ''.join(b1), ''.join(b2)

def crossover(board1, board2):
    # Perform crossover at a random position
    x = random.randint(1, 7)
    return board1[x:] + board2[:x], board1[:x] + board2[x:]

def fitness(board):
    # Calculate the number of attacks for a given board state
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(int(board[i]) - int(board[j])) == j - 1:
                attacks += 1
    return attacks

def genetic_algorithm(generations, initial_pop):
    pq = [(fitness(board), board) for board in initial_pop]
    
    for i in range(generations):
        pq.sort()
        f1, b1 = pq.pop(0)
        f2, b2 = pq.pop(0)
        
        if f1 == 0 or f2 == 0:
            print("Goal state =", b1 if f1 == 0 else b2, "Attacks =", i + 1)
            return
        
        new_pop = [*crossover(b1, b2), *mutate(b1, b2), *mutate(b2, b1)]
        pq.extend([(fitness(child), child) for child in new_pop])
    
    pq.sort()
    print("Most evolved state =", pq[0][0], "Generations =", generations, "Attacks =", pq[0][1])

# Example usage:
genetic_algorithm(1000, ["32752411", "24748552"])
genetic_algorithm(1000, ["17581234", "56782463"])
