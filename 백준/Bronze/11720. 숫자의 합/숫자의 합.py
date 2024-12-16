import sys

N = int(sys.stdin.readline().rstrip())
numbers = sys.stdin.readline().rstrip()
sumation = 0

for i in range(N):
    sumation += int(numbers[i])
    
print(sumation)