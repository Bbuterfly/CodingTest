import sys
sys.setrecursionlimit(10000)

def dfs(start, depth, N, M, result, visited):
    if depth == M:
        print(" ".join(map(str, result)))
        return

    for i in range(start, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i + 1, depth + 1, N, M, result, visited)
            result.pop()
            visited[i] = False

# N, M : 자연수, 1<=N, M<=8
def main():
    N, M = map(int, sys.stdin.readline().split())
    
    visited = [False] * (N + 1)
    result = []
    dfs(1, 0, N, M, result, visited)

if __name__ == "__main__":
    main()