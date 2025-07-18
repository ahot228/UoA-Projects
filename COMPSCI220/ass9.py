import sys
sys.setrecursionlimit(100000)

def read_graphs():
    graphs = []
    lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "":
            i += 1
            continue
        n = int(line)
        i += 1
        if n == 0:
            break
        graph = [[] for _ in range(n)]
        for v in range(n):
            if i >= len(lines):
                break
            line = lines[i].strip()
            if line:
                graph[v] = sorted(map(int, line.split()))
            else:
                graph[v] = []
            i += 1
        graphs.append(graph)
    return graphs

def dfs(u, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)

def reverse_graph(graph):
    n = len(graph)
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rev[v].append(u)
    for lst in rev:
        lst.sort()
    return rev

def kosaraju_scc(graph):
    n = len(graph)
    visited = [False] * n
    finish_order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        finish_order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    rev = reverse_graph(graph)
    visited = [False] * n
    count = 0

    def dfs2(u):
        visited[u] = True
        for v in rev[u]:
            if not visited[v]:
                dfs2(v)

    for u in reversed(finish_order):
        if not visited[u]:
            dfs2(u)
            count += 1
    return count

def count_weak_components(graph):
    n = len(graph)
    visited = [False] * n
    undirected = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            undirected[u].append(v)
            undirected[v].append(u)
    for adj in undirected:
        adj.sort()

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, undirected, visited)
            count += 1
    return count

def main():
    graphs = read_graphs()
    for graph in graphs:
        weak = count_weak_components(graph)
        strong = kosaraju_scc(graph)
        print(f"Weak Components: {weak}")
        print(f"Strong Components: {strong}")

if __name__ == "__main__":
    main()