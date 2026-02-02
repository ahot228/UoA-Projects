import random

n = 30
print(n)

for i in range(n):
    num_neighbors = random.randint(2, 4)
    neighbors = []
    
    for _ in range(num_neighbors):
        neighbor = random.randint(0, n-1)
        if neighbor != i and neighbor not in neighbors:
            neighbors.append(neighbor)
    
    while len(neighbors) < 2:
        neighbor = random.randint(0, n-1)
        if neighbor != i and neighbor not in neighbors:
            neighbors.append(neighbor)
    
    print(" ".join(map(str, neighbors)))

print(0) 