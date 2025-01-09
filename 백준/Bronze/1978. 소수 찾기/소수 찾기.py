import sys

n = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for l in lst:
    if l < 2:
        continue
    elif l == 2 or l == 3:
        count += 1
    
    for div in range(2, int(l ** 0.5)+1):
        if l%div == 0:
            break
        
        
        if l%div != 0 and div == int(l ** 0.5):
            count += 1
            
print(count)