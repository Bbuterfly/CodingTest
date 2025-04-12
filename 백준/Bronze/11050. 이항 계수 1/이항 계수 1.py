import sys

def combination(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k+1):
        result *= n
        result //= i
        n -= 1
    return result

def main():
    '''
    N : 자연수, 1<=N<=10
    K: 정수, 0<=K<=N
    '''
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(combination(N, K))

if __name__ == "__main__":
    main()