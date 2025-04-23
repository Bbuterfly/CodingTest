import sys
from collections import Counter

def brute_force(B, heights):
    min_h, max_h = 0, 256
    cases = []
    for height in range(max_h, min_h-1, -1):
        current = B
        time = 0
        
        for key, cnt in heights.items():
            if key > height:
                diff = key - height
                current += diff * heights[key]
                time += 2* diff * heights[key]
            elif key < height:
                diff = height - key
                current -= diff * heights[key]
                time += diff * heights[key]
    
        if current >= 0:
            cases.append([time, height])

    return min(cases, key= lambda x: (x[0], -x[1]))

# N, M : 가로/세로의 길이, 1<=M,N<=5*10^2
# B : 가지고 있는 블록의 수, 0<=B<=6.5*10^7
def main():
    N, M, B = map(int, sys.stdin.readline().rstrip().split())
    matrix = [sys.stdin.readline() for _ in range(N)]
    heights = Counter()
    
    for m in matrix:
        heights += Counter(map(int, m.split()))
    
    time, height = brute_force(B, heights)
    print(f"{time} {height}")
    
if __name__ == "__main__":
    main()