bobSpan = input()
bob = 'bob'
count = 0
isOccur = True
start = 0
while isOccur:
    a = bobSpan.find(bob, start)

    if a ==- 1:
        isOccur = False
    else:
        count += 1
        start = a + 1
print("Number of times bob occurs is: {}".format(count))