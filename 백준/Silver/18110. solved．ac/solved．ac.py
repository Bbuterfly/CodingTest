import sys
from math import floor

def custom_round(x):
    return floor(x + 0.5)

# n : 난이도의 의견 개수, 1<=n<=3*10^5
# 난이도는 1~30 정수
def main():
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return
    
    scores = [int(sys.stdin.readline()) for _ in range(n)]
    outliers = custom_round(n * 0.15)
    scores.sort()
    trim = scores[outliers:n-outliers]
    
    if not trim:
        print(0)
    else:
        print(custom_round(sum(trim) / len(trim)))

if __name__ == "__main__":
    main()