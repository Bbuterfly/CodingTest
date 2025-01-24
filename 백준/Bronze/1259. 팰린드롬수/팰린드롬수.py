while True:
    number = input().rstrip()
    if number == '0':
        break
    
    print('yes') if number == number[::-1] else print('no')