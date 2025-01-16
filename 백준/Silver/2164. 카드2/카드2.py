from collections import deque

def main():
    numbers = deque([i for i in range(int(input()), 0, -1)])

    while len(numbers) != 1:
        numbers.pop()
        numbers.appendleft(numbers.pop())

    print(numbers.pop())
    
if __name__ == '__main__':
    main()