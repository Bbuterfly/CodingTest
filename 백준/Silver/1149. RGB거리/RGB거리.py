import sys

# N : 집의 수, 2<=N<=10^3
# 둘째 줄부터 N개의 줄에 각 집의 R, G, B 비용이 주어짐. 비용은 1000보다 작거나 같은 자연수
def main():
    input = sys.stdin.readline
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = houses[0]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]
        
    print(min(dp[N-1]))

if __name__ == "__main__":
    main()