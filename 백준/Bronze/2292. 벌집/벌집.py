def main():
    '''
    N : 방의 수, 1<=N<=10^9
    '''
    N = int(input())
    
    if N == 1:
        print(1)
        return
    elif N > 1 and N <= 7:
        print(2)
        return
    
    tot = 7
    count = 2
    while not (tot < N and N <= tot + 6 * count):
        tot += 6*count
        count += 1
    
    print(count+1)

if __name__ == "__main__":
    main()