import sys

def max_non_adjacent_sum(arr):
    """Classic DP: maximum sum of non-adjacent elements."""
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    dp1, dp2 = 0, arr[0]
    for x in arr[1:]:
        dp1, dp2 = dp2, max(dp2, dp1 + x)
    return dp2

def circular_max_sum(arr):
    """Solve circular version by considering two cases:
    1. Exclude first element
    2. Exclude last element
    """
    if len(arr) == 1:
        return arr[0]
    return max(max_non_adjacent_sum(arr[1:]), max_non_adjacent_sum(arr[:-1]))

def main():
    lines = sys.stdin.read().strip().splitlines()
    for line in lines:
        jewels = list(map(int, line.split()))
        total = sum(jewels)
        d1 = circular_max_sum(jewels)
        d2 = total - d1
        print(d1, d2)

if __name__ == "__main__":
    main()