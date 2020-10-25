num = int(input())


if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "Not prime")

            break
    else:
        print(num, "Prime")


else:
    print(num, "Not prime")