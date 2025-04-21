def tiling():
    mem = [0] * 1001
    mem[1], mem[2], mem[3] = 1, 3, 5
    for i in range(4, 1001):
        if i%2:
            mem[i] = mem[i-1] * 2 - 1
        else:
            mem[i] = mem[i-1] * 2 + 1
    
    return mem

# n : 2xn 타일의 길이, 1<=n<=10^3
def main():
    n = int(input())
    print(tiling()[n]%10007)

if __name__ == "__main__":
    main()