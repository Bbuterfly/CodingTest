import sys

def main():
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    sum_list = [0] * (N+1)
    
    for i in range(1, N+1):
        sum_list[i] = sum_list[i-1] + number_list[i-1]
    
    sum_idxs = sys.stdin.read().splitlines()
    answer_list = []
    for idxs in sum_idxs:
        start, end = map(int, idxs.split())
        
        answer_list.append(str(sum_list[end] - sum_list[start-1]))

    sys.stdout.write("\n".join(answer_list))
    
if __name__ == "__main__":
    main()