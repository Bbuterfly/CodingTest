import sys

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

tot_max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cards = lst[i] + lst[j] + lst[k]
            
            if cards <= m and cards > tot_max:
                tot_max = cards
                
print(tot_max)