a = input()
b = a.split(",")
list1 = [int(x) for x in b]
odd = []

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        pass
    else:
        odd.append(list1[i])


print(odd)