x = int(input())
d = []
def ggg(x):
    global j
    for i in range(1,x + 1):
        if i % 5 == 0 or i % 7 == 0:
            f = str(i)
            print(f, end=',')
            d.append(f)
            l = len(d)

    print('')
    print("There are {} numbers divisible by 5 or 7.".format(l))

ggg(x)





         x = int(input())
d = []
def ggg(x):
    global j
    for i in range(1,x + 1):
        if i % 5 == 0 or i % 7 == 0:
            f = str(i)
            print(f, end=',')
            d.append(f)
            l = len(d)

    print('')
    print("There are {} numbers divisible by 5 or 7.".format(l))

ggg(x)





