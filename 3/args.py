'''
a, *b , c = (1,5,6,7)

print(a,b,c)




def ar(*args):
    s = 0
    for i in args:
        s += i

    return s

print(ar(1,5,6))
'''


def g(*args):
	print(*args)

g(1,34,5,6)