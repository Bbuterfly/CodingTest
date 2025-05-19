import sys
from collections import defaultdict
import heapq

def clean(heap, counter):
    while heap and counter[heap[0][1]] == 0:
        heapq.heappop(heap)

# T : 테스트 케이스의 수
# k : Q에 적용할 연산의 개수, 1<=k<=10^6
def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        k = int(input())
        min_h = []
        max_h = []
        counter = defaultdict(int)
        
        for _ in range(k):
            op, val = input().split()
            val = int(val)

            if op == 'I':
                heapq.heappush(min_h, (val, val))
                heapq.heappush(max_h, (-val, val))
                counter[val] += 1

            elif op == 'D':
                if val == 1:
                    clean(max_h, counter)
                    if max_h:
                        v = heapq.heappop(max_h)[1]
                        counter[v] -= 1
                else:
                    clean(min_h, counter)
                    if min_h:
                        v = heapq.heappop(min_h)[1]
                        counter[v] -= 1

        clean(min_h, counter)
        clean(max_h, counter)

        if not min_h or not max_h:
            print("EMPTY")
        else:
            print(max_h[0][1], min_h[0][0])

if __name__ == "__main__":
    main()