def tiling(n):
    mem = [0] * (n + 1)
    mem[1] = 1
    if n >= 2:
        mem[2] = 3
        
    for i in range(3, n+1):
        mem[i] = mem[i-1] + 2 * mem[i-2]
        mem[i] %= 10007
        
    return mem[n]

# n : 2xn 타일의 길이, 1<=n<=10^3
def main():
    n = int(input())
    print(tiling(n))

if __name__ == "__main__":
    main()