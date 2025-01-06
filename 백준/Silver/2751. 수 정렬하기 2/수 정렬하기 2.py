import sys

n = int(input())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort()

print('\n'.join(map(str, lst)))