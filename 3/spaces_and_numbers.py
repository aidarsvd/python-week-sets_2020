a = 1
s = ' '
m = 5
for _ in range(5):
    print(s * m, a)
    a += 1
    m -= 1
h = 1
s = ' '
m = 5

for _ in range(5):
    print(s * m, end='')
    m -= 1
    for _ in range(h):
        print(h, end='')
    print('')
    h += 1



