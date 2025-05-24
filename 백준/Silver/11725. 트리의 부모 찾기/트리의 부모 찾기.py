import sys
from collections import deque

def bfs(start, graph, visited, parent):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parent[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)

# N : 노드의 개수, 2<=N<=10^5
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어짐
def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    bfs(1, graph, visited, parent)
    
    for i in range(2, N + 1):
        print(parent[i])

if __name__ == "__main__":
    main()