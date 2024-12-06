# 0 <= cacheSize <= 30
# len(cities) <= 10^5, elements(cities) <= 20

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    dq = deque()
    
    for city in cities:
        city = city.lower()
        if city in dq:
            dq.remove(city)
            dq.append(city)
            answer += 1
            continue
            
        if len(dq) != cacheSize:
            dq.append(city)
            answer += 5
        else:
            dq.popleft()
            dq.append(city)
            answer += 5

    return answer
