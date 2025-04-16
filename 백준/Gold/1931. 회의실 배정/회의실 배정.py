import sys

def main():
    '''
    첫째 줄 N : 회의의 수, 1<=N<=10^5
    둘째 줄 부터 N+1줄까지 회의의 정보, 공백 사이로 회의 시작시간과 끝나는 시간이 주어짐
    '''
    N = int(sys.stdin.readline().rstrip())
    meeting_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    meeting_list.sort(key=lambda x:(x[1], x[0]))
    
    count = 0
    last = 0
    for start, end in meeting_list:
        if start >= last:
            count += 1
            last = end
    
    print(count)

if __name__ == "__main__":
    main()