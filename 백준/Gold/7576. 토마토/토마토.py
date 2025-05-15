import sys
from collections import deque

def bfs(M, N, box):
    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))
                
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
                
    max_day = 0
    for row in box:
        for value in row:
            if value == 0:
                return -1
            
            max_day = max(max_day, value)
            
    return max_day -1

# M, N : 상자의 크기, 2<=M, N<=10^3
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸
def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    
    print(bfs(M, N, box))

if __name__ == "__main__":
    main()