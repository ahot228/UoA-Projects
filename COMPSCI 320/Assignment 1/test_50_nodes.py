import random

# Generate a test case with 50 nodes
n = 50
print(n)

# Create a sparse graph (each node connects to 2-4 random neighbors)
for i in range(n):
    # Each node connects to 2-4 random neighbors
    num_neighbors = random.randint(2, 4)
    neighbors = []
    
    # Add some random neighbors
    for _ in range(num_neighbors):
        neighbor = random.randint(0, n-1)
        if neighbor != i and neighbor not in neighbors:
            neighbors.append(neighbor)
    
    # Ensure we have at least 2 neighbors
    while len(neighbors) < 2:
        neighbor = random.randint(0, n-1)
        if neighbor != i and neighbor not in neighbors:
            neighbors.append(neighbor)
    
    print(" ".join(map(str, neighbors)))

print(0)  # Termination 