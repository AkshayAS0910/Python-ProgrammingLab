n = int(input("enter a number : "))
factors = []
for i in range(n):
    if(n%(i+1)==0):
        factors.append(i+1)

print("Factors of {} is {}".format(n,factors))