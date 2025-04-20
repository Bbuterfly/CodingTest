import sys
from collections import defaultdict

def get_number_cases(fashion):
    tot = 1
    
    for key in fashion.keys():
        tot *= (fashion[key] + 1)
        
    return tot - 1

def main():
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