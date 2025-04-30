import sys
import heapq

# N : 연산의 개수, 1<=N<=10^5
def main():
    N = int(sys.stdin.readline())
    
    heap = []
    for _ in range(N):
        operation = int(sys.stdin.readline())
        if operation != 0:
            heapq.heappush(heap, (abs(operation), operation))
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)

if __name__ == "__main__":
    main()