import sys

def min_max_disgust(n, slop_A, slop_B):
    slop_A.sort()
    slop_B.sort()

    def can_make_lunches(max_disgust):
        i, j = 0, len(slop_B) - 1
        count = 0
        while i < len(slop_A) and j >= 0:
            if slop_A[i] + slop_B[j] <= max_disgust:
                count += 1
                i += 1
                j -= 1
            else:
                j -= 1
        return count >= n

    low = min(slop_A) + min(slop_B)
    high = max(slop_A) + max(slop_B)
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        if can_make_lunches(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer if answer != -1 else "Hungry"


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    slop_A = list(map(int, input_lines[1].split()))
    slop_B = list(map(int, input_lines[2].split()))
    print(min_max_disgust(n, slop_A, slop_B))