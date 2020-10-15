h = 22
s = '\\'
m = 0
s1 = '/'
m1 = 0

for _ in range(6):
    print(s * m, end='')
    m += 2
    for _ in range(h):
        print("!", end='')

    print(s1 * m1, end='')
    m1 += 2
    print('')

    h -= 4
h = 22
s = '\\'
m = 0
s1 = '/'
m1 = 0

for _ in range(6):
    print(s * m, end='')
    m += 2
    for _ in range(h):
        print("!", end='')

    print(s1 * m1, end='')
    m1 += 2
    print('')

    h -= 4

