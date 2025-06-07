import sys

def dfs(depth, N, M, numbers, visited, result):
    if depth == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(numbers[i])
            dfs(depth + 1, N, M, numbers, visited, result)
            result.pop()
            visited[i] = False

# N : 1-N까지의 자연수, 1<=N<=8
# M : N개의 자연수 중 M개를 고른 수열, 1<=M<=N<=8
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    visited = [False] * N
    dfs(0, N, M, numbers, visited, [])

if __name__ == "__main__":
    main()