
num = int(input())

factorial = 1


if num < 0:
   print("Negative integer.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Factorial of {} is {}.".format(num, factorial))
num = int(input())

factorial = 1


if num < 0:
   print("Negative integer.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Factorial of {} is {}.".format(num, factorial))