data = list()
from collections import defaultdict

for _ in range(3):
    data.append(int(input()))
    
sum_str = str(data[0] * data[1] * data[2])
dictionary = defaultdict(int)
for s in sum_str:
    dictionary[s] += 1
    
for i in range(10):
    print(dictionary[str(i)])