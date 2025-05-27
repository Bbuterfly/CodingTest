import sys

def power(A, B, C):
    if B == 0:
        return 1
    if B == 1:
        return A % C
    
    temp = power(A, B // 2, C)
    if B % 2 == 0:
        return (temp ** 2) % C
    else:
        return ((temp ** 2) * A) % C



# A, B, C : 2,147,483,647 이하의 자연수
def main():
    A, B, C = map(int, sys.stdin.readline().split())
    
    print(power(A, B, C))

if __name__ == "__main__":
    main()