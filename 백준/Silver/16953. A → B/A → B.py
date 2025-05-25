import sys
from collections import deque

def bfs(A, B):
    queue = deque()
    queue.append((A, 1))
    
    while queue:
        curr, cnt = queue.popleft()
        if curr == B:
            return cnt
        
        op1 = curr * 2
        if op1 <= B:
            queue.append((op1, cnt + 1))
            
        op2 = int(str(curr) + '1')
        if op2 <= B:
            queue.append((op2, cnt + 1))
            
    return -1
    
def main():
    A, B = map(int, sys.stdin.readline().split())
    
    print(bfs(A, B))

if __name__ == "__main__":
    main()