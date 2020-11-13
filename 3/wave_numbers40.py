a = '_-^-'
s = '-'
v = 1
for _ in range(40):
    print(s, end='')

print('')

for i in range(10):
    print(a, end='')

print('')

for _ in range(20):
    for j in range(2):
        print(v, end='')
    if v < 9:
        v+=1
    else:
        v = 0

print('')

for _ in range(40):
    print(s, end='')
