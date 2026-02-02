import sys

input_lines = sys.stdin.read().splitlines()
i = 0

while i < len(input_lines):
    line = input_lines[i].strip()
    if line == "0":
        break

    n = int(line)
    edge_count = 0

    for j in range(1, n + 1):
        neighbors = list(map(int, input_lines[i + j].strip().split()))
        edge_count += len(neighbors)

    print(edge_count // 2)
    i += n + 1