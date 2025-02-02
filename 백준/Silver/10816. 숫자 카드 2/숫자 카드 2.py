import sys
from collections import Counter

def main():
    inputs = sys.stdin.readlines()
    cnt = Counter(inputs[1].split())
    
    print(" ".join(str(cnt[key]) for key in inputs[3].split()))
        
if __name__ == '__main__':
    main()