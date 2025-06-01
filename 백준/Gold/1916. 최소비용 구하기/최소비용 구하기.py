import sys
import heapq

def dijkstra(start, n, graph):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for to, weight in graph[now]:
            next_cost = cost + weight
            if next_cost < dist[to]:
                dist[to] = next_cost
                heapq.heappush(heap, (next_cost, to))

    return dist

# N : N개의 도시, 1<=N<=10^3
# M : M개의 버스, 1<=M<=10^5
# 셋 째줄 부터 버스의 비용이 입력, 0<=버스비용<10^5
def main():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start, end = map(int, input().split())
    dist = dijkstra(start, n, graph)
    print(dist[end])

if __name__ == "__main__":
    main()