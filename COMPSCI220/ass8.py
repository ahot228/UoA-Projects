from collections import deque, defaultdict
import sys

def bfs_with_classification(n, edges, source):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * n
    distance = [-1] * n
    predecessor = ['-'] * n
    level_sets = defaultdict(list)
    arc_classification = defaultdict(list)

    visit_order = []
    queue = deque()

    visited[source] = True
    distance[source] = 0
    queue.append(source)

    while queue:
        u = queue.popleft()
        visit_order.append(u)

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)
                arc_classification[u].append((v, "tree"))
            else:
                if predecessor[u] != v:
                    arc_classification[u].append((v, "cross"))

    # Fill level sets
    for i in range(n):
        if distance[i] != -1:
            level_sets[distance[i]].append(i)

    # Output
    print("BFS Visit Order:", ' '.join(map(str, visit_order)))
    print("Distances:", ' '.join(map(str, distance)))
    print("Predecessors:", ' '.join(str(predecessor[i]) for i in range(n)))
    for level in sorted(level_sets):
        print(f"Level {level}:", ' '.join(map(str, sorted(level_sets[level]))))
   
    print("Arc Classifications:")
    for u in visit_order:
        for v in adj[u]:
            for tgt, typ in arc_classification[u]:
                if tgt == v:
                    print(f"({u},{v}): {typ}")
                    break

# Read input from stdin
def main():
    input_lines = sys.stdin.read().splitlines()
    n, m = map(int, input_lines[0].split())
    edges = [tuple(map(int, line.split())) for line in input_lines[1:m+1]]
    source = int(input_lines[m+1])
    bfs_with_classification(n, edges, source)

if __name__ == "__main__":
    main()