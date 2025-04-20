import sys
from collections import defaultdict

def get_number_cases(fashion):
    tot = 1
    
    for key in fashion.keys():
        tot *= (fashion[key] + 1)
        
    return tot - 1

def main():
    '''
    tc : 첫째 줄의 테스트 케이스의 수, 1<=tc<=10^2
    n : 해빈이가 가진 의상의 수, 0<=n<=30
    다음 n 개의 줄에서 공백을 기준으로 의상의 이름과 종류가 입력
    '''
    
    tc = int(input())
    
    answer = []
    for _ in range(tc):
        n = int(input())
        fashion = defaultdict(int)
        
        for _ in range(n):
            _, kind = sys.stdin.readline().rstrip().split()    
            fashion[kind] += 1
            
        answer.append(get_number_cases(fashion))
    
    sys.stdout.write("\n".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()