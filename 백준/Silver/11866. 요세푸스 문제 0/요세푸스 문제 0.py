import sys
from collections import deque

# N : N명의 사람, 1<=N<=10^3
# K : 제거할 칸의 수
def main():
    N, K = map(int, sys.stdin.readline().split())
    
    queue = deque(range(1, N+1))
    answer = []
    while queue:
        queue.rotate(-K + 1)
        answer.append(queue.popleft())
        
    print("<" + ", ".join(map(str, answer)) + ">")

if __name__ == "__main__":
    main()