import sys

# N : 물품의 수, 1<=N<=10^2
# K : 준서가 버틸 수 있는 무게, 1<=K<=10^5
# 두 번째 줄부터 N개의 줄에 W와 V가 주어짐
# W : 물건의 무게, 1<=W<=10^5
# V : 물건의 가치, 1<=V<=10^3
def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    
    dp = [0] * (K + 1)
    
    for w, v in items:
        for weight in range(K, w - 1, -1):
            dp[weight] = max(dp[weight], dp[weight - w] + v)
        
    print(dp[K])

if __name__ == "__main__":
    main()