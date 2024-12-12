# 1 <= x <= y <= 10^5
# DFS? BFS? DP

from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    
    mem = [float('inf')]*(y + 1) # 0~y까지의 배열
    mem[x] = 0 # 시작
    
    for idx in range(x, y+1):
        if mem[idx] == float('inf'): # 나올 수 없는 수 처리
            continue
    
        if idx * 2 <= y:
            mem[idx * 2] = min(mem[idx * 2], mem[idx]+1)
        
        if idx * 3 <= y:
            mem[idx * 3] = min(mem[idx * 3], mem[idx]+1)
        
        if idx + n <= y:           
            mem[idx + n] = min(mem[idx + n], mem[idx]+1)
    
    return mem[y] if mem[y] != float('inf') else -1
