import sys

def search(M, N, x, y):
    k = x
    while k <= M * N:
        if (k - y) % N == 0:
            return k
        k += M
        
    return -1

# T : 테스트 개수
# 각 테스트 데이터는 한 줄로 입력받으며 정수 M, N, x, y가 주어짐
# 1<= M, N, <= 4 * 10^4
# 1<= x <= M
# 1<= y <= N
def main():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        print(search(M, N, x, y))

if __name__ == "__main__":
    main()