string = input()
lst = ['-1'] * 26

for i, s in enumerate(string):
    if lst[ord(s)-97] != '-1':
        continue
    lst[ord(s)-97] = str(i)

print(" ".join(lst))