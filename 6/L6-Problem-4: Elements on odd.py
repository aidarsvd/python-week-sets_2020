a = input()
b = a.split(",")
list1 = [int(x) for x in b]
odd = []

odd.append(list1[0])
for i in range(1, len(list1)):

    if i % 2 == 0:
        odd.append(list1[i])
    else:
        pass

print(odd)