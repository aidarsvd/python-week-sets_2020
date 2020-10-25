a = input()
b = a.split(",")
list1 = [str(x) for x in b]

c = input()

if c in list1:
    print("True")
else:
    print("False")