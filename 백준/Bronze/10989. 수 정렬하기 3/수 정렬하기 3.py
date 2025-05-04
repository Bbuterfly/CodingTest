import sys

# N : 수의 개수, 1<=N<=10^7
# 두 번째 줄부터 10^4이하의 자연수가 주어짐
def main():
    N = int(sys.stdin.readline())
    count = [0] * 10001
    
    for _ in range(N):
        num = int(sys.stdin.readline())
        count[num] += 1
        
    for i in range(1, 10001):
        if count[i] > 0:
            for _ in range(count[i]):
                print(i)

if __name__ == "__main__":
    main()