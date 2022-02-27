import math
def fact(n):
    return(math.factorial(n))
num = int(input('Enter the Number'))
f = fact(num)
print('Factorial of num', num, 'is', f)