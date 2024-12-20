lst = input().split()

ascend = '12345678'
descend = '87654321'

order = "".join(lst)

if order == ascend:
    print('ascending')
elif order == descend:
    print('descending')
else:
    print('mixed')