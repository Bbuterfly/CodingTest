import sys
import heapq

def main():
    N = int(sys.stdin.readline().rstrip())

    answer = []
    max_heap = []
    heapq.heapify(max_heap)
    
    for _ in range(N):
        data = int(sys.stdin.readline().rstrip())
        
        if data == 0:
            if max_heap:
                answer.append(str(abs(heapq.heappop(max_heap))))
            else:
                answer.append('0')
        else:
            heapq.heappush(max_heap, -data)
    
    sys.stdout.write("\n".join(answer) + "\n")
            
if __name__ == "__main__":
    main()