import sys

n = int(sys.stdin.readline().rstrip())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort()

for e in lst:
    print(e)