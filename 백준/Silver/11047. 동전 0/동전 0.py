import sys

def main():
    '''
    N : 동전의 개수, 1<=N<=10
    K : 만들려는 금액, 1<=K<=10^8
    '''
    N, K = map(int, sys.stdin.readline().rstrip().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    coins.reverse()
    
    tot = 0
    for coin in coins:
        if K < coin:
            continue
        
        div = K // coin
        tot += div
        K = K%coin
    
    print(tot)

if __name__ == "__main__":
    main()