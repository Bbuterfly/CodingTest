import sys

# N : N * N 크기의 배열, 1<=N<=2^10
# M : M개의 쿼리, 1<=M<=10^5
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [[0] * (N + 1)]
    for _ in range(N):
        arr.append([0] + list(map(int, input().split())))
    
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = (
                prefix[i-1][j] + prefix[i][j-1] 
                - prefix[i-1][j-1] + arr[i][j]
            )
    
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        result = (
            prefix[x2][y2]
            - prefix[x1-1][y2]
            - prefix[x2][y1-1]
            + prefix[x1-1][y1-1]
        )
        print(result)

if __name__ == "__main__":
    main()