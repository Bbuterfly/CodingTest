import sys

def main():
    xyList = sys.stdin.readlines()[1:]
    xyList.sort(key=lambda y: int(y.split()[1]))
    xyList.sort(key=lambda x: int(x.split()[0]))
    
    print(''.join(xyList))
    
if __name__ == "__main__":
    main()