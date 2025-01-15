import sys
from collections import defaultdict

n = int(input())
dd = defaultdict(list)

for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    dd[int(age)].append(name)
    
for i in sorted(dd.keys()):
    while len(dd[i]):
        print(i, dd[i].pop(0))