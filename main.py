def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial (n-1)                                      
n=3
print("Number", n)
print("Factorial:", factorial(n))