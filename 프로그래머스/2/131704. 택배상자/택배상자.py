# 1 <= len(order) <= 10^6
# 1 <= order[i] <= len(order), order[i]의 값 중복 x
# 스택 이용

def solution(order):
    stack = []
    length = len(order)
    index = 0
    for i in range(1, length+1):
        stack.append(i)
        
        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1
    
    return index