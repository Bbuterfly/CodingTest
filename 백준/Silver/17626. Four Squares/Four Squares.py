import sys
import math

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

# n : 자연수 n, 1<=n<=5 * 10^4
def main():
    n = int(sys.stdin.readline())
    
    if is_square(n):
        print(1)
        return
    
    for i in range(1, int(n**0.5) + 1):
        if is_square(n - i**2):
            print(2)
            return
        
    tmp = n
    while tmp % 4 == 0:
        tmp //= 4
    if tmp % 8 == 7:
        print(4)
    else:
        print(3)   
    
if __name__ == "__main__":
    main()