import sys
input = sys.stdin.read
n = int(input())

mylist = [17]
for i in range(n - 1):
    mylist.append(mylist[i] * 17 % 65521)

indices = list(range(n))
indices.sort(key=lambda x: mylist[x])

print(mylist[indices[n // 2]])