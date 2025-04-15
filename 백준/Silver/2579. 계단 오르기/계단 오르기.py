import sys

def main():
    '''
    n : 계단의 개수, 0<n<=3*10^2
    m : 계단의 점수, 0<m<=10^4
    '''
    n = int(sys.stdin.readline().rstrip())
    
    mem = [0] * n
    stair_scores = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    
    if n == 1:
        print(stair_scores[0])
        return
    if n == 2:
        print(stair_scores[0] + stair_scores[1])
        return
    
    mem[0] = stair_scores[0]
    mem[1] = stair_scores[0] + stair_scores[1]
    mem[2] = max(stair_scores[0] + stair_scores[2], stair_scores[1] + stair_scores[2])
    
    for i in range(3, n):
        mem[i] = max(mem[i-2], mem[i-3] + stair_scores[i-1]) + stair_scores[i]
        
    print(mem[n-1])

if __name__ == "__main__":
    main()