import sys

N = int(input())
data = [sys.stdin.readline().rstrip().split() for _ in range(N)]

for i in range(N):
    length = len(data[i][1])
    for j in range(length):
        print(data[i][1][j] * int(data[i][0]), end='')
    print()