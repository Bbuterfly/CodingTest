import sys
from collections import deque

def bfs(N, K):
    MAX = 100001
    visited = [-1] * MAX
    dq = deque()
    dq.append(N)
    visited[N] = 0

    while dq:
        current = dq.popleft()

        if current == K:
            return visited[current]

        next_pos = current * 2
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current]
            dq.appendleft(next_pos)

        next_pos = current - 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            dq.append(next_pos)

        next_pos = current + 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            dq.append(next_pos)

# N : 수빈이의 현재 점, 0<=N<=10^5
# K : 동생의 점, 0<=K<=10^5
def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    print(bfs(N, K))

if __name__ == "__main__":
    main()