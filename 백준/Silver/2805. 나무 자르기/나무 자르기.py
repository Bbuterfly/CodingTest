import sys

def is_possible(trees, target, mid):
    total = 0
    for tree in trees:
        if tree > mid:
            total += (tree - mid)
    
    return total >= target

def main():
    '''
    1<=N<=10^6
    1<=M<=2*10^9
    '''
    N, M= map(int, sys.stdin.readline().rstrip().split())
    trees =  list(map(int, sys.stdin.readline().rstrip().split()))
    
    left, right = 0, max(trees)
    result = 0
    
    while left <= right:
        mid = (left + right)//2
        
        if is_possible(trees, M, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    print(result)

if __name__ == "__main__":
    main()