import sys
from collections import deque

def bfs(start, graph, N):
    visited = [-1] * (N + 1)
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    
    return sum(visited[1:])

# N : 유저의 수, 2<=N<=10^2
# M : 친구 관계의 수, 1<=M<=5*10^3
def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    result = []
    for i in range(1, N + 1):
        result.append((bfs(i, graph, N), i))
        
    result.sort()
    print(result[0][1])

if __name__ == "__main__":
    main()