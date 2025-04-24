import sys
from collections import deque

def bfs(N, M, matrix, start):
    queue = deque()
    queue.append(start)
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cnt = 0
    
    while queue:
        y, x = queue.popleft()
        
        if matrix[y][x] == 'P':
            cnt += 1
        for d in direction:
            dy, dx = d[0], d[1]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] != 'X' and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
        
    return cnt
# N, M : 캠퍼스의 크기 N, M
# 1<=N, M<=6*10^2
# 둘째 줄 부터 N개의 줄에는 캠퍼스의 정보, O : 빈공간, X : 벽, I : 도연이, P : 사람
def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    matrix = [sys.stdin.readline().rstrip() for _ in range(N)]
    
    doyeon = None
    for col_idx, col in enumerate(matrix):
        for row_idx, row in enumerate(col):
            if row == 'I':
                doyeon = (col_idx, row_idx)
                break
    
    cnt = bfs(N, M, matrix, doyeon)
    print('TT') if cnt == 0 else print(cnt)

if __name__ == "__main__":
    main()