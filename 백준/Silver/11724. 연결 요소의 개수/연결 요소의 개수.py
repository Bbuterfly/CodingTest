import sys
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v]
    
    while queue:
        v = queue.popleft()
        for neigbor in graph[v]:
            if not visited[neigbor]:
                visited[neigbor] = True
                queue.append(neigbor)
def main():
    '''
    1<=N<=10^3 : N은 정점의 수
    0<=M<= N*(N-1)/2 : M은 간선의 개수
    1<= u, v <= N, 단 u =/ v : 간선의 양 끝점 u, v
    '''
    N, M = map(int, sys.stdin.readline().rstrip().split())

    vertexs = sys.stdin.readlines()
    
    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]
    
    for vertex in vertexs:
        u, v = map(int, vertex.split())
        
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(graph, i, visited)
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()