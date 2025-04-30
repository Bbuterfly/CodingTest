import sys

# K : 입력의 개수, 1<=K<=10^5
# 둘째 줄 부터 K개의 정수 입력, 범위는 1~10^6
# 0일 경우 가장 최근에 쓴 수를 지우고 아닐 경우 해당 수를 씀. 0일 경우 지울 수 있는 수가 있음을 보장
def main():
    K = int(sys.stdin.readline())
    stack = []
    for _ in range(K):
        integer = int(sys.stdin.readline())
        
        if not integer:
            stack.pop()
        else:
            stack.append(integer)
            
    print(sum(stack))

if __name__ == "__main__":
    main()