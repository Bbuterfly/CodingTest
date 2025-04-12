import sys
import math

def main():
    '''
    N : 자연수, 1<=N<=10
    K: 정수, 0<=K<=N
    '''
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(math.factorial(N) // (math.factorial(N-K) * math.factorial(K)))

if __name__ == "__main__":
    main()