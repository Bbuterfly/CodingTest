import sys
from collections import deque

def bfs(x, y, graph, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    return graph[N-1][M-1]

# N, M : N * M의 미로, 2<= N, M <= 10^2
# 이동할 수 있는 칸 : 1, 없는 칸 : 2
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    
    print(bfs(0, 0, graph, N, M))

if __name__ == "__main__":
    main()