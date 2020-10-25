arr = []
n=int(input())
def Fib(n):

  if arr[n] != -1:
    return arr[n]
  if n == 0:
    arr[0] = 0
    return 0
  elif n == 1:
    arr[1] = 1
    return 1  
  else:
    arr[n] = Fib(n-1) + Fib(n-2)
    return arr[n]

for i in range(n+1):
    arr.append(-1)
Fib(n)

arr.remove(0)
print(arr)