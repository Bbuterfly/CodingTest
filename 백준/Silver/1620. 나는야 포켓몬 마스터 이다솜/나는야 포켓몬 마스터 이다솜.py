import sys

# 1 <= N, M <= 10^5
# 단 N, M은 자연수

def main():
    input_data = sys.stdin.read().split('\n')
    N, M = map(int, input_data[0].split())
    
    name2num = {}
    num2name = {}
    for i in range(1, N+1):
        value = input_data[i]
        num2name[str(i)] = value
        name2num[value] = str(i)
        
    output = []
    for i in range(N+1, N+ 1 + M):
        search = input_data[i]
        output.append(name2num.get(search, num2name.get(search)))
    
    sys.stdout.write('\n'.join(output) + '\n')
    
if __name__ == '__main__':
    main()