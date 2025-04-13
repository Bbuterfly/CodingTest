import sys

def brute_force(N):
    num = 666
    cnt = 0
    
    while True:
        if '666' in str(num):
            cnt += 1
            if cnt == N:
                return num
        num += 1

def main():
    '''
    N : N번 째 영화, N<=10^4, 자연수
    '''
    N = int(sys.stdin.readline().rstrip())
    print(brute_force(N))

if __name__ == "__main__":
    main()