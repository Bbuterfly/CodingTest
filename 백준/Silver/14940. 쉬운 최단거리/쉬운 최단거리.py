import sys
from collections import deque

def bfs(n, m):
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    v = ()
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 2:
                v = (j, i)
        
    dist = [[-1] * m for _ in range(n)]
    queue = deque()
    queue.append(v)
    col, row = v[0], v[1]
    dist[col][row] = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x = queue.popleft()
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0<= ny < n and 0<= nx < m:
                if graph[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
    
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 0:
                print(0, end=' ')
            else:
                print(dist[j][i], end=' ')
        print()

def main():
    '''
    n : 세로의 길이, 2<=n<=10^3
    m : 가로의 길이, 2<=m<=10^3
    '''
    n, m = map(int, sys.stdin.readline().rstrip().split())
    bfs(n, m)

if __name__ == "__main__":
    main()