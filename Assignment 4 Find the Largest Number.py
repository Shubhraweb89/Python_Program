a=int(input("Enter 1st no: "))
b=int(input("Enter 2st no: "))
c=int(input("Enter 3st no: "))
if(a>b & a>c):        ##Checking for the largest number
    print(a)
elif(b>a & b>c):      ##Checking for the largest number
    print(b)
else:
    print(c)