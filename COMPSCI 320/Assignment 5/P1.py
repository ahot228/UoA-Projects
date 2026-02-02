import sys
from collections import deque

# ---------- Edmonds–Karp (BFS-based Max-Flow) ----------
def bfs(cap, flow, s, t, parent):
    n = len(cap)
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v in range(n):
            if not visited[v] and cap[u][v] - flow[u][v] > 0:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return True
                q.append(v)
    return False

def maxflow(cap, s, t):
    n = len(cap)
    flow = [[0]*n for _ in range(n)]
    parent = [-1]*n
    max_flow = 0
    while bfs(cap, flow, s, t, parent):
        # Find bottleneck
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, cap[u][v] - flow[u][v])
            v = u
        # Update flow
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        max_flow += path_flow
    return max_flow

# ---------- Main Logic ----------
def main():
    data = sys.stdin.read().strip().splitlines()
    idx = 0
    while idx < len(data):
        n = int(data[idx].strip())
        if n == 0:
            break
        idx += 1

        adj = [[] for _ in range(n)]
        for i in range(n):
            if idx < len(data) and data[idx].strip():
                adj[i] = list(map(int, data[idx].split()))
            idx += 1

        # Build capacity matrix (unit capacity for each undirected edge)
        cap = [[0]*n for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                cap[u][v] = 1

        best = 0
        for s in range(n):
            for t in range(s+1, n):
                best = max(best, maxflow(cap, s, t))
        print(best)

if __name__ == "__main__":
    main()