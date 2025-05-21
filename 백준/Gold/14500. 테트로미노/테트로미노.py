import sys
sys.setrecursionlimit(10000)

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, total, visited, board, N, M, max_val):
    global answer
    
    if total + max_val * (4 - depth) <= answer:
        return
    
    if depth == 4:
        answer = max(answer, total)
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny], visited, board, N, M, max_val)
            visited[nx][ny] = False

def check_t_shape(x, y, board, N, M):
    global answer
    
    t_shapes = [
        [(0, 0), (-1, 0), (0, -1), (0, 1)],  # ㅗ
        [(0, 0), (-1, 0), (1, 0), (0, 1)],   # ㅏ
        [(0, 0), (1, 0), (0, -1), (0, 1)],   # ㅜ
        [(0, 0), (-1, 0), (1, 0), (0, -1)]   # ㅓ
    ]

    for shape in t_shapes:
        try:
            total = 0
            for dx_, dy_ in shape:
                nx, ny = x + dx_, y + dy_
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    raise IndexError
                total += board[nx][ny]
            answer = max(answer, total)
        except IndexError:
            continue

# N, M : 세로, 가로의 크기, 4<=N, M<=5*10^2
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    max_val = max(map(max, board))
    
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j], visited, board, N, M, max_val)
            visited[i][j] = False
            check_t_shape(i, j, board, N, M)

    print(answer)

if __name__ == "__main__":
    main()