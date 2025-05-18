import sys
from collections import deque

def bfs(graph, visited):
    distance = [0] * 101
    
    queue = deque()
    queue.append(1)
    visited[1] = True
    
    while queue:
        curr = queue.popleft()
        
        for dice in range(1, 7):
            next = curr + dice
            if next > 100:
                continue
            
            if graph[next] != 0:
                next = graph[next]
            
            if not visited[next]:
                visited[next] = True
                distance[next] = distance[curr] + 1
                queue.append(next)
                
            if next == 100:
                return distance[100]

# N : 사다리의 수, 1<=N<=15
# M : 뱀의 수, 1<=M<=15
# 둘째 줄부터 N개의 사다리의 정보 x, y가 주어짐(x<y) : x번 칸에 도착하면 y번 칸으로 이동
# 다음 M개의 줄에서 뱀의 정보를 의미하는 u,v가 주어짐(u>v) : u번 칸에 도착하면 v번 칸으로 이동
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [0] * 101
    
    for _ in range(N + M):
        a, b = map(int, input().split())
        graph[a] = b
        visited = [False] * 101
        
    print(bfs(graph, visited))

if __name__ == "__main__":
    main()