a = input()

b = a.split(",")
list1 = [int(x) for x in b]
list1.sort()

max = len(list1)
max -= 1

print(list1[max])


