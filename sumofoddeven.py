max=int(input("please enter the maximum value: "))

even_Sum=0
odd_Sum=0
for num in range(1,max+1):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
print("The sum of Even numbers 1 to {0} = {1}".format(num,even_Sum))
print("The sum of Oddn numbers 1 to {0} = {1}".format(num,odd_Sum))