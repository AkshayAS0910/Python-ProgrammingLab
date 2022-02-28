def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input('Enter the first Number '))
b=int(input('Enter the second Number '))
GCD=gcd(a,b)
print(GCD)