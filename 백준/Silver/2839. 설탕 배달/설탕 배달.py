import sys

def minimum_sugar(N):
    mem = [5001] * (N + 1)
    mem[0] = 0
    
    for i in range(1, N+1):
        if i >= 3:
            mem[i] = min(mem[i], mem[i-3] + 1)
        if i >= 5:
            mem[i] = min(mem[i], mem[i-5] + 1)
            
    return mem[N] if mem[N] != 5001 else -1

# N : 설탕의 총 kg, 3<=N<=5*10^3
def main():
    N = int(sys.stdin.readline().rstrip())
    
    print(minimum_sugar(N))

if __name__ == "__main__":
    main()