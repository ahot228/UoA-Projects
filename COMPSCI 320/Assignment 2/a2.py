import sys

def find(parent, x):
    """Find latest available slot <= x."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def min_penalty(tasks):
    tasks.sort(key=lambda x: -x[1])

    max_deadline = max(d for d, _ in tasks)
    parent = list(range(max_deadline + 1))

    total_penalty = 0

    for d, p in tasks:
        available = find(parent, min(d, max_deadline))
        if available > 0:
            parent[available] = find(parent, available - 1)
        else:
            total_penalty += p
    return total_penalty


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    tasks = [(int(data[i]), int(data[i+1])) for i in range(1, 2*n, 2)]
    print(min_penalty(tasks))