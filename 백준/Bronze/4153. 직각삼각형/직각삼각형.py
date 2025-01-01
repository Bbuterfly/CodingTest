while 1:
    legs = sorted(list(map(int, input().split())))
    
    if legs == [0, 0, 0]:
        break
    
    if legs[-1] ** 2 == legs[0] ** 2 + legs[1] ** 2:
        print('right')
    else:
        print('wrong')