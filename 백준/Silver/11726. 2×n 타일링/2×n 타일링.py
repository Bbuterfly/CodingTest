def main():
    n = int(input())
    
    if n == 1:
        print('1')
        exit()
    elif n == 2:
        print('2')
        exit()
        
    a, b = 1, 2
    
    for _ in range(3, n+1):
        current = (a + b) % 10007
        a, b = b, current
        
    print(b)

if __name__ == "__main__":
    main()