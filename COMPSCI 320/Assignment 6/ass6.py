from collections import defaultdict, deque

# ---------- Dinic's Max Flow ----------
class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, len(self.adj[v]), cap])
        self.adj[v].append([u, len(self.adj[u]) - 1, 0])

    def bfs(self, s, t, level):
        queue = deque([s])
        level[s] = 0
        while queue:
            v = queue.popleft()
            for nxt, rev, cap in self.adj[v]:
                if cap > 0 and level[nxt] < 0:
                    level[nxt] = level[v] + 1
                    queue.append(nxt)
        return level[t] >= 0

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.adj[v])):
            it[v] = i
            nxt, rev, cap = self.adj[v][i]
            if cap > 0 and level[v] + 1 == level[nxt]:
                d = self.dfs(nxt, t, min(f, cap), level, it)
                if d > 0:
                    self.adj[v][i][2] -= d
                    self.adj[nxt][rev][2] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9
        while True:
            level = [-1] * self.n
            if not self.bfs(s, t, level):
                break
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0:
                    break
                flow += f
        return flow

# ---------- Adapter Reachability ----------
def build_reachability(adapters, all_types):
    graph = defaultdict(list)
    for a, b in adapters:
        graph[a].append(b)
    reachable = {t: set() for t in all_types}
    for t in all_types:
        # BFS from each plug type
        seen = {t}
        q = deque([t])
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        reachable[t] = seen
    return reachable

# ---------- Main ----------
def main():
    import sys
    data = sys.stdin.read().strip().split()
    idx = 0
    T = int(data[idx]); idx += 1

    results = []
    for _ in range(T):
        n = int(data[idx]); idx += 1
        outlets = [data[idx + i] for i in range(n)]
        idx += n

        m = int(data[idx]); idx += 1
        laptops = [data[idx + i] for i in range(m)]
        idx += m

        k = int(data[idx]); idx += 1
        adapters = [(data[idx + 2*i], data[idx + 2*i + 1]) for i in range(k)]
        idx += 2 * k

        all_types = set(outlets + laptops + [a for a, b in adapters] + [b for a, b in adapters])
        reachable = build_reachability(adapters, all_types)

        # Build flow graph
        S = 0
        laptop_start = 1
        outlet_start = 1 + m
        Tnode = outlet_start + n
        dinic = Dinic(Tnode + 1)

        for i in range(m):
            dinic.add_edge(S, laptop_start + i, 1)
        for j in range(n):
            dinic.add_edge(outlet_start + j, Tnode, 1)

        for i in range(m):
            for j in range(n):
                lt = laptops[i]
                ot = outlets[j]
                if ot == lt or ot in reachable.get(lt, set()):
                    dinic.add_edge(laptop_start + i, outlet_start + j, 1)

        maxflow = dinic.max_flow(S, Tnode)
        results.append(str(m - maxflow))

    print("\n".join(results))

if __name__ == "__main__":
    main()