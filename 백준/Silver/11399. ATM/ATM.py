import sys

def main():
    input_data = sys.stdin.read().splitlines()
    
    lst = sorted(list(map(int, input_data[1].split())))
    
    tot, times = 0, 0
    for time in lst:
        times += time
        tot += times
        
    sys.stdout.write(f"{tot}")
    
if __name__ == "__main__":
    main()