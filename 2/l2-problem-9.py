try:
    age = int(input())

    if age >= 19 and age <= 149:
        print("Old enough!")

    elif age <= 18 and age >= 0:
        print("Too young.")

    else:
        print('Incorrect age.')

except ValueError:
    print('Incorrect age.')
    print('Incorrect age.')