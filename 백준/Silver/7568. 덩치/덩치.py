import sys

def main():
    '''
    N : 전체 사람의 수, 2<=N<=50
    이어지는 N + 1번째 줄 부터 N명의 사람의 몸무게(x)와 키(y)가 공백을 두고 주어짐 : 10<=x,y<=200
    '''
    N = int(input())
    person_info = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    ranks = []
    
    for i in range(N):
        rank = 1
        for j in range(N):
            if i == j:
                continue
            if person_info[j][0] > person_info[i][0] and person_info[j][1] > person_info[i][1]:
                rank += 1
        
        ranks.append(rank)
    
    print(" ".join(map(str, ranks)))
        
if __name__ == "__main__":
    main()