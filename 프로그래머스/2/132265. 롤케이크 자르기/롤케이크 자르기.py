# 1 <= len(topping) <= 10^5
# 1 <= topping[i] <= 1^4
# Binary Search로 진행한다면?? time cpmplexity O(log_2n)
from collections import Counter

def solution(topping):
    #if len(set(topping))%2 != 0: # 토핑의 종류가 홀수이면 나눌 방법이 없음
    #    return 0

    answer = 0
    eat = set()
    topping_dict = Counter(topping)
    
    for i in topping:
        topping_dict[i] -= 1
        if topping_dict[i] == 0:
            del topping_dict[i]
        eat.add(i)
        
        if len(topping_dict) == len(eat):
            answer += 1
        
    return answer



    