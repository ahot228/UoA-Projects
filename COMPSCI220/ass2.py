import sys

nests = [tuple(map(int, line.strip().split())) for line in sys.stdin]
n = len(nests)
    
max_length = 0
best_common_egg = float('inf')

for common_egg in range(1, 6):
    left = 0
    for right in range(n):
        if common_egg not in nests[right]:
            left = right + 1
            continue
            
        length = right - left + 1
        if length > max_length or (length == max_length and common_egg < best_common_egg):
            max_length = length
            best_common_egg = common_egg
print(max_length)
print(best_common_egg)