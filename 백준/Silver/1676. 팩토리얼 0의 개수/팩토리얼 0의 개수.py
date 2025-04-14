import sys

def count(N):
    cnt = 0
    while N >= 5:
        N //= 5
        cnt += N
    return cnt

def main():
    '''
    N : N!, 0<=N<=5*10^2
    '''
    N = int(sys.stdin.readline().rstrip())
    print(count(N))

if __name__ == "__main__":
    main()