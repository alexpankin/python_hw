from itertools import cycle, count

for el in count(10, 10):
    print(el)
    if el > 15:
        break


my_list = [12, 34, 45, 56]
c = 0
for el in cycle(my_list):
    c += 1
    print(el)
    if c > 15:
        break