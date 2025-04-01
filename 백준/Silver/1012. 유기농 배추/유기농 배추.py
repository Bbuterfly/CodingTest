import sys
from collections import deque

def bfs(graph, v, visited, m, n):
    x, y = v
    queue = deque([v])
    visited[y][x] = True
    
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

def main():
    T = int(input())
    
    for _ in range(T):
        m, n, k = map(int, sys.stdin.readline().split())
        
        matrix = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        tot = 0
        
        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            matrix[y][x] = 1
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and not visited[i][j]:
                    bfs(matrix, (j, i), visited, m, n)
                    tot += 1
        
        print(tot)
        
if __name__ == "__main__":
    main()