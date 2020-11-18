a = input()
array = []
for i in range(len(a)):
    array.append(a[i])

u = 0

for i in range(len(array)):
    if array[i].lower() in ('a', 'e', 'i', 'o', 'u'):
        u += 1
    else:
        pass

print(u)