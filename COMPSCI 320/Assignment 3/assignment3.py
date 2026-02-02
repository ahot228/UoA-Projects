import sys
import bisect

def search_in_matrix(matrix, m, n, target):
    """
    Efficient search in a row/column-sorted matrix.
    Returns (row, col) of the first occurrence with lowest row, then lowest column,
    or None if not found.
    """
    # Use staircase search for efficiency
    row, col = 0, n - 1
    while row < m and col >= 0:
        val = matrix[row][col]
        if val == target:
            # Found target, use binary search to find leftmost occurrence in this row
            # Only search up to current column since we know target exists at current position
            leftmost_col = bisect.bisect_left(matrix[row], target, 0, col + 1)
            return (row, leftmost_col)
        elif val > target:
            col -= 1
        else:  # val < target
            row += 1
    return None


def solve():
    """Process input line by line to avoid memory issues"""
    out_lines = []
    
    while True:
        try:
            # Read first line of test case
            line = input().strip()
            if not line:
                continue
                
            m, n, k = map(int, line.split())
            if m == 0 and n == 0 and k == 0:
                break

            # Read matrix
            matrix = []
            for _ in range(m):
                row = list(map(int, input().split()))
                matrix.append(row)

            # Process queries
            for _ in range(k):
                target = int(input())
                ans = search_in_matrix(matrix, m, n, target)
                out_lines.append("None" if ans is None else f"{ans[0]} {ans[1]}")
                
        except EOFError:
            break
    
    # Print all results at once
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()