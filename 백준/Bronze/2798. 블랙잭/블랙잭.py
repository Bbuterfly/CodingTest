from itertools import combinations
import bisect
import sys

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

tot_max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        two_sum = lst[i] + lst[j]
        
        if two_sum >= m:
            continue
        
        target = m - two_sum
        idx = bisect.bisect_right(lst, target, j + 1, n) - 1
        
        if idx > j:
            tot_sum = two_sum + lst[idx]
            tot_max = max(tot_max, tot_sum)
                
print(tot_max)