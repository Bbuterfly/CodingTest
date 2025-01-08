import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
t, p = map(int, sys.stdin.readline().rstrip().split())

tot = 0
for i in lst:
    if i == 0:
        continue
    
    if i<t or i==t:
        tot += 1
    elif i%t == 0:
        tot += i//t
    else:
        tot += (i//t + 1)

print(tot)
print(n//p, n%p)