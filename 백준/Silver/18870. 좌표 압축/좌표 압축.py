import sys

def main():
    '''
    N : X의 개수, 1<=N<=10^6
    Xi : 공백으로 구분된 정수, -10^9<=Xi<=10^9
    '''
    N = int(sys.stdin.readline().rstrip())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
    
    set_X = sorted(set(X))
    dict_X = {}
    for i, x in enumerate(set_X):
        dict_X[x] = i
        
    for i, x in enumerate(X):
        X[i] = dict_X[x]
        
    X = list(map(str, X))
    sys.stdout.write(" ".join(X) + "\n")

if __name__ == "__main__":
    main()