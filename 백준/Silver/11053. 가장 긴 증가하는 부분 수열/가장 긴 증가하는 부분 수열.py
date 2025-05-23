import sys

# N : 수열 A의 크기, 1<=N<=10^3
# 둘째 줄에 수열 A가 주어짐. 1<=A_i<=10^3
def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    dp = [1] * N
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(max(dp))

if __name__ == "__main__":
    main()