import sys
from collections import deque
sys.setrecursionlimit(10**7)

class Dinic:
    __slots__ = ("n", "g", "level", "it")
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]  # adjacency: list of edges (to, cap, rev_index)
        self.level = [0]*n
        self.it = [0]*n

    def add_edge(self, u, v, cap):
        # forward edge index = len(self.g[u])
        self.g[u].append([v, cap, len(self.g[v])])
        # reverse edge
        self.g[v].append([u, 0, len(self.g[u])-1])

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        dq = deque()
        dq.append(s)
        level[s] = 0
        while dq:
            u = dq.popleft()
            for e in self.g[u]:
                v, cap, _ = e
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    if v == t:
                        return True
                    dq.append(v)
        return level[t] >= 0

    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.g[u])):
            self.it[u] = i
            v, cap, rev = self.g[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, f if f < cap else cap)
                if pushed:
                    # subtract on forward
                    self.g[u][i][1] -= pushed
                    # add on reverse
                    self.g[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                flow += pushed
        return flow

def build_vertex_split_base(n, adj):
    """Return list of base edges (u, v, cap) and N = 2*n.
       For each vertex v: add edge v_in->v_out with cap=1.
       For each undirected original edge (a,b): add a_out->b_in and b_out->a_in with cap=INF_EDGE.
    """
    edges = []
    # vertex internal capacity = 1
    for v in range(n):
        edges.append((v, v + n, 1))

    # Add undirected edges as directed both ways, but avoid double-adding duplicates.
    seen = set()
    INF_EDGE = n  # big enough: any cut <= n
    for u in range(n):
        for v in adj[u]:
            a, b = (u, v) if u <= v else (v, u)
            if (a, b) in seen:
                continue
            seen.add((a, b))
            # add both directed edges for the undirected original edge:
            # u_out -> v_in and v_out -> u_in
            edges.append((u + n, v, INF_EDGE))
            edges.append((v + n, u, INF_EDGE))
    return edges, 2*n

def gomory_hu_vertex_disjoint(n, adj):
    # Build base graph edges (vertex-split)
    base_edges, N = build_vertex_split_base(n, adj)
    parent = [0] * n
    capval = [0] * n

    for s in range(1, n):
        t = parent[s]
        dinic = Dinic(N)
        # add all base edges
        for (u, v, c) in base_edges:
            if c > 0:
                dinic.add_edge(u, v, c)

        s_node = s + n  # s_out
        t_node = t      # t_in

        f = dinic.max_flow(s_node, t_node)
        capval[s] = f

        # find reachable nodes from s_node in residual graph
        visited = [False]*N
        stack = [s_node]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            for v, cap, _ in dinic.g[u]:
                if cap > 0 and not visited[v]:
                    stack.append(v)

        # For nodes i whose parent == t and whose out-node is reachable, set parent[i] = s
        for i in range(s+1, n):
            if parent[i] == t and visited[i + n]:
                parent[i] = s

    # capval[0] stays 0; maximum congestion is max(capval)
    return max(capval) if n > 0 else 0

def solve():
    data = sys.stdin.read().strip().splitlines()
    idx = 0
    out_lines = []
    L = len(data)
    while idx < L:
        line = data[idx].strip()
        if not line:
            idx += 1
            continue
        n = int(line)
        idx += 1
        if n == 0:
            break
        adj = [[] for _ in range(n)]
        for i in range(n):
            if idx < L:
                ln = data[idx].strip()
                if ln:
                    # neighbors given as integers separated by spaces
                    adj[i] = list(map(int, ln.split()))
                idx += 1
            else:
                break
        res = gomory_hu_vertex_disjoint(n, adj)
        out_lines.append(str(res))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()