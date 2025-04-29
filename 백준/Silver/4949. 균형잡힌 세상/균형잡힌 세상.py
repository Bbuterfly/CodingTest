import sys

def is_balance(string):
    stack = []
    for char in string:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 'no'
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 'no'
            stack.pop()
        
    return 'no' if stack else 'yes'

def main():
    string = None
    
    while True:
        string = sys.stdin.readline().rstrip()
        if string == ".":
            break
        
        print(is_balance(string))

if __name__ == "__main__":
    main()