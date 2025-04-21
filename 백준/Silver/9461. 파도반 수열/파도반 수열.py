import sys

def padovan():
    mem = [0] * 101
    mem[1], mem[2], mem[3], mem[4], mem[5] = 1, 1, 1, 2, 2
    
    for i in range(6, 101):
        mem[i] = mem[i-1] + mem[i-5]
        
    return mem

# T : 테스트 케이스의 수
# N : 구해야하는 파도반의 수, 1<=N<=10^2
def main():
    T = int(input())
    
    answer = []
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        answer.append(padovan()[N])
        
    sys.stdout.write("\n".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()