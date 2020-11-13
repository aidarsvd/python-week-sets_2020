name = input()
sur = input()

print('Your credentials are {} {}.' .format(name, sur))

p = []

n = len(name)
s = len(sur)
g = 1

if n >= s:
    while g <= s:
        p.append(name[g - 1])
        p.append(sur[g - 1])
        g += 1

    else:
        while g<=n:
            p.append(name[g-1])
            g += 1
else:
    while g<= n:
        p.append(name[g-1])
        p.append(sur[g-1])
        g += 1

    else:
        while g<= s:
            p.append(sur[g-1])
            g += 1

pp = ''.join(p)

print("Your password is " +pp+'.')



