import sys
from collections import deque

def bfs(N, K):
    max_limit = 100001
    visited = [False] * max_limit
    queue = deque()
    queue.append((N, 0))
    visited[N] = True
    
    while queue:
        current, time = queue.popleft()
        
        if current == K:
            return time
        
        for next in [current - 1, current +1, current * 2]:
            if 0<= next < max_limit and not visited[next]:
                visited[next] = True
                queue.append((next, time + 1))

def main():
    '''
    N : 수빈이의 현재 점, 0<=N<=10^5
    K : 동생의 현재 점, 0<=K<=10^5
    '''
    N, K = map(int, sys.stdin.readline().split())
    print(bfs(N, K))

if __name__ == "__main__":
    main()