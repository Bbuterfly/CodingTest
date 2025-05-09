import sys

# n : 1-n까지의 정수, 1<=n<=10^5
def main():
    n = int(sys.stdin.readline())
    target = [int(sys.stdin.readline()) for _ in range(n)]
    
    stack = []
    result = []
    curruent = 1
    possible = True
    
    for num in target:
        while curruent <= num:
            stack.append(curruent)
            result.append('+')
            curruent += 1
        
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            possible = False
            break
        
    if possible:
        print("\n".join(result))
    else:
        print('NO')

if __name__ == "__main__":
    main()