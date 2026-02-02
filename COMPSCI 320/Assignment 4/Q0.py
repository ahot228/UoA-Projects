import sys


lines = sys.stdin.read().strip().splitlines()
S1 = list(map(int, lines[0].split()))
S2 = list(map(int, lines[1].split()))

n1 = len(S1)
for x in S2:
    print(n1 + x)