import sys

def bfs(N, r, c):
    if N == 0:
        return 0
    
    half = 2 ** (N - 1)
    if r < half and c < half:
        return bfs(N-1, r, c)
    elif r < half and c >= half:
        return half * half + bfs(N-1, r, c-half)
    elif r >= half and c < half:
        return 2 * half * half + bfs(N-1, r-half, c)
    else:
        return 3 * half * half + bfs(N-1, r-half, c-half)

def main():
    '''
    N : 2^N x 2^N의 2차원 배열, 1<=n<=15
    r : 행, 0<=r
    c : 열, c<=2^N
    '''
    N, r, c = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(N, r, c))

if __name__ == "__main__":
    main()