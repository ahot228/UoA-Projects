import sys
import heapq

def dijkstra(n, edges, source):
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # Initialize distances
    dist = [float('inf')] * n
    dist[source] = 0

    # Priority queue: (distance, vertex)
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist

def main():
    # Read input
    input_lines = sys.stdin.read().strip().split('\n')
    n, m = map(int, input_lines[0].split())
    edges = []
    for line in input_lines[1:m+1]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
    source = int(input_lines[m+1])

    # Compute shortest delivery times
    delivery_times = dijkstra(n, edges, source)

    # Output
    for i, time in enumerate(delivery_times):
        print(f"Warehouse {i}: Delivery time = {time}")

if __name__ == "__main__":
    main()