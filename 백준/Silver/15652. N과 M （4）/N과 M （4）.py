import sys

def dfs(start, depth, N, M, result):
    if depth == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        result.append(i)
        dfs(i, depth + 1, N, M, result)
        result.pop()

# N : 1-N까지의 자연수, 1<=N<=8
# M : N개의 자연수 중 M개를 고른 수열, 1<=M<=N<=8
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    dfs(1, 0, N, M, [])

if __name__ == "__main__":
    main()