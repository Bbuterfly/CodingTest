import sys
sys.setrecursionlimit(10000)

def dfs(x, y, graph, visited, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = True
    count = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny, graph, visited, n)
    
    return count

# n : 지도의 크기, 1<=n<=25
# 지도에서 0 : 집이 없는 곳, 1 : 집이 있는 곳
def main():
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                house_count = dfs(i, j, graph, visited, n)
                result.append(house_count)
    
    result.sort()
    print(len(result))
    for r in result:
        print(r)

if __name__ == "__main__":
    main()