import sys
from collections import deque

# T : 테스트 케이스의 수, 1<=T<=10^2
# 각 테스트 케이스의 첫 줄은 수행할 함수 p가 주어진다. 1<= len(p) <= 10^5
# 그 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. 1<= n <= 10^5
def main():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        operations = input().strip()
        n = int(input())
        arr = input().strip()
        
        if n == 0:
            deq = deque()
        else:
            deq = deque(arr[1:-1].split(','))
    
        is_error = False
        is_reversed = False
        
        for op in operations:
            if op == 'R':
                is_reversed = not is_reversed
            elif op == 'D':
                if len(deq) == 0:
                    print('error')
                    is_error = True
                    break
                
                if is_reversed:
                    deq.pop()
                else:
                    deq.popleft()
                
        if not is_error:
            if is_reversed:
                deq.reverse()
                
            print("[" + ",".join(deq) + "]")

if __name__ == "__main__":
    main()