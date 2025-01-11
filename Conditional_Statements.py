#basic syntax
age=int(input("Enter the users age"))
if(age>18):
    print("you can drive")
elif(age<0):
    print("invalid age")
else:
    print("you cant drive")

#finding maximun numbers from the 3 numbers entered by user
n1=int(input("Enter number"))
n2=int(input("Enter number"))
n3=int(input("Enter number"))
if(n1>n2 and n1>n3 ):
    print(n1)
elif(n2>n1 and n2>n3 ):
    print(n2)
elif(n3>n2 and n3>n1 ):
    print(n3)