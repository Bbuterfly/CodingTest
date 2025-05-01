import sys
from collections import deque

def bfs(start, graph, N):
    visited = [0] * N
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for next in range(N):
            if graph[current][next] == 1 and not visited[next]:
                visited[next] = 1
                queue.append(next)
                
    return visited    
    
# N : 정점의 개수, 1<=N<=10^2
# 둘째 줄부터 N개의 인접 행렬
# 1인 경우 간선이 존재, 0인 경우 없음
def main():
    N = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    result = []
    for i in range(N):
        result.append(bfs(i, graph, N))
    
    for row in result:
        print(" ".join(map(str, row)))
        
if __name__ == "__main__":
    main()