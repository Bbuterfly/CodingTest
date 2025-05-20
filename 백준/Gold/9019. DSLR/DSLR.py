import sys
from collections import deque

def D(n):
    return (n * 2) % 10000

def S(n):
    return 9999 if n == 0 else n -1

def L(n):
    return (n % 1000) * 10 + (n // 1000)

def R(n):
    return (n % 10) * 1000 + (n // 10)

def bfs(start, target):
    visited = [False] * 10000
    prev = [-1] * 10000
    how = [''] * 10000
    
    queue = deque([start])
    visited[start] = True

    while queue:
        curr = queue.popleft()

        if curr == target:
            break

        for op, func in [('D', D), ('S', S), ('L', L), ('R', R)]:
            next_num = func(curr)
            if not visited[next_num]:
                visited[next_num] = True
                prev[next_num] = curr
                how[next_num] = op
                queue.append(next_num)

    result = []
    cur = target
    while cur != start:
        result.append(how[cur])
        cur = prev[cur]
    return ''.join(reversed(result))

# T : 테스트케이스의 수
# a, b : 레지스터의 초기값과 최종 값, 0<=a, b<10^4
def main():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        a, b = map(int, input().split())
        print(bfs(a, b))

if __name__ == "__main__":
    main()