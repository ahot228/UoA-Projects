import sys

def list_to_matrix(adj_list, n):
    matrix = [[0] * n for _ in range(n)]
    for i, neighbors in enumerate(adj_list):
        for j in neighbors:
            matrix[i][j] = 1
    return matrix

def matrix_to_list(matrix, n):
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

def compute_degrees(matrix, n):
    in_degrees = [0] * n
    out_degrees = [0] * n
    total_edges = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                out_degrees[i] += 1
                in_degrees[j] += 1
                total_edges += 1

    return in_degrees, out_degrees, total_edges

def process_graphs():
    lines = sys.stdin.read().splitlines()
    idx = 0
    mode = lines[idx].strip()
    idx += 1

    while idx < len(lines):
        if lines[idx].strip() == '0':
            break

        n = int(lines[idx])
        idx += 1

        if mode == 'list':
            adj_list = []
            for _ in range(n):
                if lines[idx].strip() == '':
                    adj_list.append([])
                else:
                    adj_list.append(list(map(int, lines[idx].split())))
                idx += 1

            matrix = list_to_matrix(adj_list, n)

            # Output matrix
            print(n)
            for row in matrix:
                print(' '.join(map(str, row)))

        elif mode == 'matrix':
            matrix = []
            for _ in range(n):
                matrix.append(list(map(int, lines[idx].split())))
                idx += 1

            adj_list = matrix_to_list(matrix, n)

            # Output list
            print(n)
            for i, neighbors in enumerate(adj_list):
                if neighbors:
                    print(f"{i}: {' '.join(map(str, neighbors))}")
                else:
                    print(f"{i}:")

        # Compute degrees
        in_deg, out_deg, total = compute_degrees(matrix, n)
        for i in range(n):
            print(f"Node {i}: in-degree = {in_deg[i]}, out-degree = {out_deg[i]}")
        print(f"Total edges = {total}\n")

        # Read mode for next graph if there is one
        if idx < len(lines) and lines[idx] in ['matrix', 'list']:
            mode = lines[idx].strip()
            idx += 1

if __name__ == "__main__":
    process_graphs()