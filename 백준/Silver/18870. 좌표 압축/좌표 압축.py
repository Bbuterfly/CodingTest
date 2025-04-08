import sys

def main():
    '''
    N : X의 개수, 1<=N<=10^6
    Xi : 공백으로 구분된 정수, -10^9<=Xi<=10^9
    '''
    N = int(sys.stdin.readline().rstrip())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
    
    uniqueX = sorted(set(X))
    mapping = {x: i for i, x in enumerate(uniqueX)}
    result = [str(mapping[x]) for x in X]
    sys.stdout.write(" ".join(result) + "\n")

if __name__ == "__main__":
    main()