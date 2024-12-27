import sys

n = int(input())
strings = list()
for _ in range(n):
    strings.append(sys.stdin.readline().rstrip())

for string in strings:
    total, count = 0, 0
    
    for s in string:
        if s == 'X':
            count = 0
        else:
            count += 1
            total += count
            
    print(total)