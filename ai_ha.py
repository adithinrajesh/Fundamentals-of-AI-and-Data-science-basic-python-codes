def is_valid_assignment(assign):
    """
    Check if the current assignment satisfies the given constraints.

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.

    Returns:
    - True if the assignment is valid, False otherwise.
    """
    a, b, c, d = assign['a'], assign['b'], assign['c'], assign['d']
    if c != -1 and d != -1 and c < d:
        return False
    if d != -1 and a != -1 and a - d != 1:
        return False
    if d != -1 and b != 1 and abs(d - b) == 1:
        return False
    if c == 3 or b == 1:
        return False

    return True

def get_unassigned_house(assign):
    """
    Find the first unassigned house in the assignment.

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.

    Returns:
    - The name of the first unassigned house.
    """
    for house, location in assign.items():
        if location == -1:
            return house

def is_goal(assign):
    """
    Check if the assignment is complete (all houses assigned).

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.

    Returns:
    - True if the assignment is complete, False otherwise.
    """
    return not (-1 in assign.values())

def dynamic_house_order(assign):
    """
    Order houses dynamically based on the number of constraints.

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.

    Returns:
    - List of house names ordered by the number of constraints.
    """
    return sorted(assign.keys(), key=lambda house: sum(1 for constraint in assign.values() if constraint != -1))

def backtrack(assign, locations):
    """
    Backtracking algorithm for the house problem.

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.
    - locations: List of available locations.

    Returns:
    - A valid color assignment for each house, or None if no solution exists.
    """
    return recursive_backtrack(assign, locations)

def recursive_backtrack(assign, locations):
    """
    Recursive part of the backtracking algorithm.

    Parameters:
    - assign: Dictionary representing the current assignment of houses to locations.
    - locations: List of available locations.

    Returns:
    - A valid color assignment for each house, or None if no solution exists.
    """
    # Counter for recursive calls
    global recursive_calls
    recursive_calls += 1

    if is_goal(assign):
        return assign

    house = get_unassigned_house(assign)

    for loc in locations:
        assign[house] = loc
        if is_valid_assignment(assign):
            result = recursive_backtrack(assign, locations)
            if result:
                return result

    assign[house] = -1
    return None

# Global counter for recursive calls
recursive_calls = 0

# Initial assignment and locations
initial_assignment = {"a": -1, 'b': -1, 'c': -1, 'd': -1}
locations = [1, 2, 3, 4]

# Solve the problem
solution = backtrack(initial_assignment, dynamic_house_order(initial_assignment))

# Print the solution and recursive calls
if solution:
    for house, location in solution.items():
        print("House =", house, " Location =", location)
    print("Recursive Calls:", recursive_calls)
else:
    print("No solution occurs")
