import math
import random

def fcost(sol):
    return sum([i**2 for i in sol])

def successors(sol, step=1.0):
    # Generate a successor by adding a random value to each element in the solution
    succ = [x + random.uniform(-step, step) for x in sol]
    return succ

def simAnnealing(initSol, initTemp, alpha, iters):
    currSol = initSol
    cost = fcost(currSol)
    sol = currSol
    minCost = cost
    temp = initTemp

    for iteration in range(iters):
        # Generate a successor solution
        neighbor = successors(currSol)
        ncost = fcost(neighbor)

        # Calculate the cost difference between the current and neighbor solutions
        costdiff = ncost - cost

        # Accept the neighbor solution if it has a lower cost or with a certain probability
        if costdiff < 0 or random.random() < math.exp(-costdiff / temp):
            currSol = neighbor
            cost = ncost

            # Update the best solution if the current cost is lower
            if cost < minCost:
                sol = currSol
                minCost = cost

        # Reduce the temperature
        temp *= alpha

    return sol, minCost

initSol = [300.0, 400.0]
initTemp = 1000.0
alpha = 0.95
iters = 500

bestSol, cost = simAnnealing(initSol, initTemp, alpha, iters)

print("\nBest Solution:", bestSol)
print("Best Cost:", cost)
