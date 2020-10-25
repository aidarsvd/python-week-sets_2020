try:
    num = int(input())

    factorial = 1

    if num < 0:
       print("error")
    elif num == 0:
       print(1)
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print(factorial)
except ValueError:
    print("error")
