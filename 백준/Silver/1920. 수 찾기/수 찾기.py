import sys

def count(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None
        
def main():
    n = int(input())
    nList = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(input())
    mList = list(map(int, sys.stdin.readline().rstrip().split()))
    nList.sort()

    for i in mList:
        print(0 if count(nList, i, 0, len(nList) - 1) == None else 1)
    
if __name__ == '__main__':
    main()