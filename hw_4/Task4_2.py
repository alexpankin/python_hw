el = [1, 3, 5, 6, 8, 14, 45, 7]
print(el)
el = [el[i] for i in range(1, len(el)) if el[i] > el[i-1]]
print(el)
