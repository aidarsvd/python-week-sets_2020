h = 1
s = '-'
m = 5
s1 = '-'
m1 = 5

for _ in range(5):
    print(s * m, end='')
    m -= 1
    for _ in range(h):
        print(h, end='')

    print(s1 * m1, end='')
    m1 -= 1
    print('')

    h += 2

