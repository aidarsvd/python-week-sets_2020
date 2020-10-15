a = '*'
s = 1
for _ in range(4):
    print(a * s)
    s += 1
def findLength(string):

    count = 0


    for i in string:
        count += 1

    return count



string = str(input())
d = findLength(string)
print("The length is {}.".format(d))
for _ in range(2):
    print(string, end='')