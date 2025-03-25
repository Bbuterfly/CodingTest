import sys

def main():
    input_data = sys.stdin.read().splitlines()
    N, M = map(int, input_data[0].split())
    
    no_heard = set(input_data[1:N+1])
    no_seen = set(input_data[N+1:N+M+1])
    
    rs = sorted(no_heard & no_seen)
    
    sys.stdout.write(f"{len(rs)}\n" + "\n".join(rs) + "\n")    
    
if __name__ == '__main__':
    main()
    
    