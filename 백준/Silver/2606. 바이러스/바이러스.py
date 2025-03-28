from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    
    return count

def main():
    computers = int(input())
    networks = int(input())
    
    graph = [[] for _ in range(computers + 1)]
    visited = [False] * (computers + 1)
    
    for _ in range(networks):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(bfs(1, visited, graph))

if __name__ == "__main__":
    main()