import itertools

# Function to calculate the total distance of a path
def calculate_distance(cities, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += cities[path[i]][path[i+1]]
    total_distance += cities[path[-1]][path[0]]  # Return to starting point
    return total_distance

# Function to solve the Traveling Salesman Problem using brute force
def tsp_bruteforce(cities):
    n = len(cities)  # Number of cities
    all_permutations = itertools.permutations(range(n))  # Get all possible paths
    min_distance = float('inf')
    best_path = None
    
    # Check all possible paths
    for path in all_permutations:
        distance = calculate_distance(cities, path)
        if distance < min_distance:
            min_distance = distance
            best_path = path
    
    return best_path, min_distance

# Example adjacency matrix for cities (distance between cities)
cities = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve the TSP
best_path, min_distance = tsp_bruteforce(cities)

# Output the result
print("Best path:", best_path)
print("Minimum distance:", min_distance)
