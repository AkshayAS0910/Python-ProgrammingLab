def fib(n):
    if (n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))

n=int(input("\nEnter the limit : "))

if(n<=0):
    print("\nenter positive number")
else:
    print("\nFibnoacci series : ")
    for i in range(n):
        print(fib(i))