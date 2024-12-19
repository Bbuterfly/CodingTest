a = 1
for _ in range(3):
    a *= int(input())

a = str(a)
for i in range(10):
    c = str(i)
    print(a.count(c))