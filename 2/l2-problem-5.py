try:
    a = float(input())

    if a == 0:
        print('0 is not odd nor even')


    elif a % 2 == 0:
        print("This number is even")

    else:
        print("This number is odd")

except ValueError:
    print("Incorrect inputs!")