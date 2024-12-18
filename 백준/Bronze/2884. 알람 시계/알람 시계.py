h, m = map(int, input().split())
hours = [hour for hour in range(0, 24)]
minutes = [minute for minute in range(0, 60)]

if m < 45:
    print(f'{hours[h-1]} {minutes[m-45]}')
else:
    print(f'{hours[h]} {minutes[m-45]}')