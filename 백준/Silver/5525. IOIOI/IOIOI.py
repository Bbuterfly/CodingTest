import sys

# N : N+1개의 I, N개의 o, 1<=N<=10^6
# M : S의 길이, 2N+1<=M<=10^6
# S : I와 O로 이루어져있는 문자열
def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    S = input().strip()
    
    count = 0
    i = 0
    pattern = 0
    
    while i < M - 1:
        if S[i:i+3] == 'IOI':
            pattern += 1
            i += 2
            
            if pattern == N:
                count += 1
                pattern -= 1
        
        else:
            i += 1
            pattern = 0
            
    print(count)

if __name__ == "__main__":
    main()