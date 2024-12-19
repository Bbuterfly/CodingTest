t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    
    if n == 1:
        print('101')
        continue
    
    y = n%h
    x = n//h
    
    if y == 0 and x < 10:
        print(f'{h}0{x}')
    elif y == 0 and x >= 10:
        print(f'{h}{x}')
    elif y > 0 and x+1 >= 10:
        print(f'{y}{x+1}')
    elif y > 0 and x+1 < 10:
        print(f'{y}0{x+1}')