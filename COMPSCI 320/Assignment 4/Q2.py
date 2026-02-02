import sys

def rotated_binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1  # keep going right to find highest index
        elif arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return result

def main():
    lines = sys.stdin.read().strip().splitlines()
    S1 = list(map(int, lines[0].split()))
    S2 = list(map(int, lines[1].split()))

    for x in S2:
        print(rotated_binary_search(S1, x))

if __name__ == "__main__":
    main()