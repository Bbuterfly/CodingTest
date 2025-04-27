import sys

# N : 점의 개수, 1<=N<=10^5
def main():
    N = int(sys.stdin.readline().rstrip())
    input_data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    
    input_data.sort(key=lambda x: (x[1], x[0]))
    output = []
    for x, y in input_data:
        output.append(f"{x} {y}")
    
    sys.stdout.write("\n".join(output) + "\n")
    
if __name__ == "__main__":
    main()