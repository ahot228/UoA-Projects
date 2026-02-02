import sys

def find_longest_snake_exact(n, adj):
    max_length = 0
    
    def can_extend(path_mask, last_vertex, new_vertex):
        if path_mask & (1 << new_vertex):
            return False
        if last_vertex != -1 and not (adj[last_vertex] & (1 << new_vertex)):
            return False
        for i in range(n):
            if path_mask & (1 << i) and i != last_vertex:
                if adj[i] & (1 << new_vertex):
                    return False
        return True
    
    def backtrack(path_mask, last_vertex, length):
        nonlocal max_length
        
        if length > 0:
            max_length = max(max_length, length)
        
        remaining = n - bin(path_mask).count('1')
        if length + remaining <= max_length:
            return
        
        if last_vertex != -1:
            neighbors = adj[last_vertex]
            for next_vertex in range(n):
                if neighbors & (1 << next_vertex) and can_extend(path_mask, last_vertex, next_vertex):
                    new_mask = path_mask | (1 << next_vertex)
                    backtrack(new_mask, next_vertex, length + 1)
        else:
            for start in range(n):
                backtrack(1 << start, start, 0)
    
    backtrack(0, -1, 0)
    return max_length

def find_longest_snake_improved(n, adj):
    def is_induced_path(path):
        if len(path) <= 1:
            return True
        for i in range(len(path) - 1):
            if not (adj[path[i]] & (1 << path[i+1])):
                return False
        for i in range(len(path)):
            for j in range(i + 2, len(path)):
                if adj[path[i]] & (1 << path[j]):
                    return False
        return True
    
    def try_greedy_path(start):
        path = [start]
        used = {start}
        
        while True:
            last = path[-1]
            best_next = -1
            
            for next_vertex in range(n):
                if next_vertex not in used and (adj[last] & (1 << next_vertex)):
                    valid = True
                    for i in range(len(path) - 1):
                        if adj[path[i]] & (1 << next_vertex):
                            valid = False
                            break
                    if valid:
                        best_next = next_vertex
                        break
            
            if best_next == -1:
                break
            
            path.append(best_next)
            used.add(best_next)
        
        return path if is_induced_path(path) else []
    
    max_length = 0
    
    for start in range(min(15, n)):
        path = try_greedy_path(start)
        if len(path) > 1:
            max_length = max(max_length, len(path) - 1)
    
    return max_length

def find_longest_snake(n, adj):
    if n <= 1:
        return 0
    
    if n <= 25:
        return find_longest_snake_exact(n, adj)
    else:
        return find_longest_snake_improved(n, adj)

def main():
    lines = sys.stdin.readlines()
    i = 0
    
    while i < len(lines):
        n = int(lines[i].strip())
        if n == 0:
            break
        
        adj = [0] * n
        for j in range(1, n + 1):
            neighbors = list(map(int, lines[i + j].split()))
            vertex = j - 1
            for neighbor in neighbors:
                adj[vertex] |= 1 << neighbor
                adj[neighbor] |= 1 << vertex
        
        result = find_longest_snake(n, adj)
        print(result)
        
        i += n + 1

if __name__ == "__main__":
    main()
