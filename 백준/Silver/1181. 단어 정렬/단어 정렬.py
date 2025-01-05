from collections import defaultdict
n = int(input())
dd = defaultdict(list)
for _ in range(n):
    i = input()
    dd[len(i)].append(i)

for key in sorted(dd.keys()):
    [print(e) for e in sorted(set(dd[key]))]