import sys

def is_vps(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'NO'
            stack.pop()
    
    return 'YES' if not stack else 'NO'

def main():
    strings = sys.stdin.readlines()[1:]

    for string in strings:
        print(is_vps(string.rstrip()))

if __name__ == '__main__':
    main()