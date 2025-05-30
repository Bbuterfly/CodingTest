import sys

# T : 테스트 케이스의 수
# n : 정수, 1<=n<=10^5
# 다음 두 줄에는 n 개의 정수가 주어짐
def main():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        
        if n == 1:
            print(max(stickers[0][0], stickers[1][0]))
            continue
            
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        dp[0][1] = dp[1][0] + stickers[0][1] 
        dp[1][1] = dp[0][0] + stickers[1][1]
        
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
            
        print(max(dp[0][n-1], dp[1][n-1]))
        
if __name__ == "__main__":
    main()