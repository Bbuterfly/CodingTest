def dp():
    mem = [0] * 12
    mem[1] = 1
    mem[2] = 2
    mem[3] = 4
    
    for i in range(4, 12):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    
    return mem
    

def main():
    T = int(input())
    
    mem = dp()
    for _ in range(T):
        n = int(input())
        print(mem[n])

if __name__ == "__main__":
    main()