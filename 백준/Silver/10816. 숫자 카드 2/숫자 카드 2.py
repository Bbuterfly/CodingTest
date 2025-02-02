import sys
from collections import Counter

def main():
    inputs = sys.stdin.readlines()
    cnt = Counter(inputs[1].rstrip().split())
    
    for key in inputs[3].rstrip().split():
        print(cnt[key], end=' ')
        
if __name__ == '__main__':
    main()