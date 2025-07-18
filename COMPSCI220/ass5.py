import heapq
import math
import sys

input_lines = sys.stdin.read().splitlines()
    
low = []  # max-heap (inverted values)
high = []  # min-heap
total_inserted = 0

for line in input_lines:
    if line == 'q':
        if low:
            print(-low[0])
    else:
        num = int(line)
        total_inserted += 1

        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)
        
        k = math.ceil(total_inserted / 3)

        while len(low) > k:
            heapq.heappush(high, -heapq.heappop(low))
        while len(low) < k:
            heapq.heappush(low, -heapq.heappop(high))