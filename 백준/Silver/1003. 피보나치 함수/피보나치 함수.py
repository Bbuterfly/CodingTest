def main():
    mem = [0] * 41
    mem[1] = 1
    mem[2] = 1

    for i in range(3, 41):
        mem[i] = mem[i-1] + mem[i-2]
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        
        if N == 0:
            print('1 0')
        elif N == 1:
            print('0 1')
        else:
            print(mem[N-1], mem[N])

if __name__ == '__main__':
    main()