import sys

white = 0
blue = 0

def count_paper(x, y, size, paper):
    global white, blue
    
    color = paper[y][x]
    
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != color:
                new_size = size//2
                count_paper(x, y, new_size, paper)
                count_paper(x + new_size, y, new_size, paper)
                count_paper(x, y + new_size, new_size, paper)
                count_paper(x + new_size, y + new_size, new_size, paper)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1
        
def main():
    N = int(sys.stdin.readline().rstrip())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    count_paper(0, 0, N, matrix)
    
    print(white)
    print(blue)    

if __name__ == "__main__":
    main()