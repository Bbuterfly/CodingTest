import sys

def count_cable(cables, length):
    return sum(cable // length for cable in cables)

def max_length(cables, N):
    low, high = 1, max(cables)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if count_cable(cables, mid) >= N:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# K : 랜선의 개수, 1<=K<=10^4
# N : 필요한 랜선의 개수, 1<=N<=10^6
def main():
    input = sys.stdin.readline
    K, N = map(int, input().split())
    
    cables = [int(input()) for _ in range(K)]
    print(max_length(cables, N))

if __name__ == "__main__":
    main()