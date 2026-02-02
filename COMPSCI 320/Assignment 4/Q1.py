import sys
import bisect

def main():
    lines = sys.stdin.read().strip().splitlines()
    S1 = list(map(int, lines[0].split()))
    S2 = list(map(int, lines[1].split()))

    for x in S2:
        # bisect_right returns insertion point → subtract 1 to get last occurrence
        idx = bisect.bisect_right(S1, x) - 1
        if idx >= 0 and S1[idx] == x:
            print(idx)
        else:
            print(-1)

if __name__ == "__main__":
    main()