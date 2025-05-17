import sys
from collections import deque

def bfs(x, y, image, color, visited, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and image[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_regions(image, N):
    visited = [[False] * N for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, image, image[i][j], visited, N)
                count += 1
    
    return count

# N : N * N 크기의 그림 : 1<=N<=10^2
# 둘째 줄부터 그림이 주어짐
def main():
    input = sys.stdin.readline
    N = int(input())
    image = [list(input().strip()) for _ in range(N)]
    
    general = count_regions(image, N)
    
    weak_color = [[c if c != 'G' else 'R' for c in row] for row in image]
    weak = count_regions(weak_color, N)
    
    print(general, weak)
    
if __name__ == "__main__":
    main()