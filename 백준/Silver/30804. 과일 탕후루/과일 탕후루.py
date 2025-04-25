import sys
from collections import defaultdict

def maximum_length(tanghuru):
    fruit_count = defaultdict(int)
    start = 0
    max_length = 0
    
    for end in range(len(tanghuru)):
        fruit = tanghuru[end]
        fruit_count[fruit] += 1
        
        while len(fruit_count) > 2:
            fruit_count[tanghuru[start]] -= 1
            if fruit_count[tanghuru[start]] == 0:
                del fruit_count[tanghuru[start]]
            start += 1

        max_length = max(max_length, end - start + 1)
    
    return max_length
            
# N : 과일의 개수, 1<=N<=2*10^5
# 둘째 줄에는 탕후루에 꽂힌 과일 배열
def main():
    N = int(sys.stdin.readline().rstrip())
    tanghuru = list(map(int, sys.stdin.readline().rstrip().split()))
    print(maximum_length(tanghuru))

if __name__ == "__main__":
    main()