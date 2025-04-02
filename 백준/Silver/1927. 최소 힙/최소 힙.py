import sys
import heapq
# N <= 10^5

def main():
    N = int(sys.stdin.readline().rstrip())
    
    heap = []
    heapq.heapify(heap)
    
    answer = []
    for _ in range(N):
        data = int(sys.stdin.readline().rstrip())
        
        if data == 0:
            if heap:
                answer.append(str(heapq.heappop(heap)))
            else:
                answer.append('0')
        else:
            heapq.heappush(heap, data)
                
    sys.stdout.write("\n".join(answer) + "\n")

if __name__ == "__main__":
    main()