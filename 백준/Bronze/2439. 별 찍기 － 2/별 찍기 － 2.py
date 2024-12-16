import sys

input = int(sys.stdin.readline())

for i in range(input):
    print(' '* (input - (i + 1)), end='')
    print('*'*(i+1))