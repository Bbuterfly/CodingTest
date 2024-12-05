# n by n 행렬
# index : element간 관계는 i : i+1

# 시간복잡도 O(n^2)
'''
def solution(n, left, right):
    answer = []
    matrix = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            matrix[i][j] = max(i, j) + 1
        
    for i in range(n):
        answer.extend(matrix[i])
    
    answer = answer[left:right+1]
    return answer
'''
# 최소 nlogn까지 줄어야함

def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        i = idx//n
        j = idx%n
        
        answer.append(max(i, j) + 1)
    
    
    return answer

