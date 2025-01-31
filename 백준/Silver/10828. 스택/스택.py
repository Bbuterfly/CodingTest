import sys

def main():
    n = int(input())
    stack = []

    for _ in range(n):
        myInput = sys.stdin.readline().rstrip().split()
        
        if myInput[0] == 'push':
            stack.append(myInput[1])
        elif myInput[0] == 'pop':
            if not stack:
                print('-1')
            else:
                print(stack.pop())
        elif myInput[0] == 'top':
            if not stack:
                print('-1')
            else:
                print(stack[-1])
        elif myInput[0] == 'size':
            print(len(stack))
        elif myInput[0] == 'empty':
            print('1') if not stack else print('0')
            
if __name__ == '__main__':
    main()