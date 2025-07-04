import sys

def main():
    input = sys.stdin.readline
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])

if __name__ == "__main__":
    main()