import sys
from collections import deque

def main():
    n = int(input())
    deq = deque()
    
    for _ in range(n):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'push':
            deq.appendleft(command[1])
        elif command[0] == 'pop':
            print(deq.pop()) if deq else print('-1')
        elif command[0] == 'size':
            print(len(deq))
        elif command[0] == 'empty':
            print('0') if deq else print('1')
        elif command[0] == 'front':
            print(deq[-1]) if deq else print('-1')
        else:
            print(deq[0]) if deq else print('-1')

if __name__ == '__main__':
    main()