try:
    age = int(input())
    if age >= 50 and age <= 100:
        print("Passed")

    elif age < 50 and age >= 0:
        print("Failed")

    else:
        print("Incorrect grade!")

except ValueError:
    print("This is not age")
try:
    age = int(input())
    if age >= 50 and age <= 100:
        print("Passed")

    elif age < 50 and age >= 0:
        print("Failed")

    else:
        print("Incorrect grade!")

except ValueError:
    print("This is not age")

