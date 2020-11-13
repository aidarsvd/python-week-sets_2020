angle = 180

a = int(input())
b = int(input())
c = int(input())

if a != 0 and b != 0 and c!= 0:
    if a + b + c == angle:
        print('It is a valid triangle.')

    else:
        print('It is not a valid triangle.')

else:
    print('It is not a valid triangle.')