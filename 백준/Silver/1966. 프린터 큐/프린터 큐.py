import sys
from collections import deque

# N : 문서의 개수, 1<=N<=10^2
# M : 궁금한 문서, 0<=M<N
def main():
    tc = int(sys.stdin.readline())
    
    for _ in range(tc):
        N, M = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        queue = deque([(i, p) for i, p in enumerate(priorities)])
        
        count = 0
        while queue:
            idx, priority = queue.popleft()
            if any(priority < other[1] for other in queue):
                queue.append((idx, priority))
            else:
                count += 1
                if idx == M:
                    print(count)
                    break       

if __name__ == "__main__":
    main()