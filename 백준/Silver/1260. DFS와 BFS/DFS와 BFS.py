import sys
from collections import deque

def dfs(graph, V, visited_dfs):
    visited_dfs[V] = True
    print(V, end=" ")
    
    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, V, visited_bfs):
    queue = deque([V])
    visited_bfs[V] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for i in graph[node]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

def main():
    '''
    1<=N<=10^3
    1<=M<=10^4
    탐색시작 정점 V
    '''
    N, M, V = map(int, sys.stdin.readline().rstrip().split())
    
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        graph[start].append(end)
        graph[end].append(start)
        
    for i in range(1, N+1):
        graph[i].sort()
    
    visited_dfs = [False] * (N+1)
    visited_bfs = [False] * (N+1)
    
    dfs(graph, V, visited_dfs)
    print()
    bfs(graph, V, visited_bfs)

if __name__ == "__main__":
    main()