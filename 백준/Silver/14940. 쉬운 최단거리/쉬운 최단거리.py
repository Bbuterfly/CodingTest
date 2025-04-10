import sys
from collections import deque

def bfs(n, m):
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # 시작점(값이 2인 곳) 찾기
    start = None
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                start = (y, x)
                break
        if start:
            break

    # 거리 배열 초기화
    dist = [[-1] * m for _ in range(n)]
    dist[start[0]][start[1]] = 0  # 시작점 거리 0
    
    queue = deque()
    queue.append(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))

    # 출력
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                print(0, end=' ')
            else:
                print(dist[y][x], end=' ')
        print()

def main():
    '''
    n : 세로 길이, 2 <= n <= 1000
    m : 가로 길이, 2 <= m <= 1000
    '''
    n, m = map(int, sys.stdin.readline().split())
    bfs(n, m)

if __name__ == "__main__":
    main()
