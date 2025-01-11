#loops are used for repetition 
#there are two types: 1. for loops 2. while loops

#lets get while loop:
#while loop executes until a conditon gets true,we dont know exactly how many times, in programs where we dont know the ending condition
#printing numbers 1-50 using while loop
i=1
while(i<=50):
    print(i)
    i+=1 

#for loop:
#EX 1
for i in range(3): #by deafult it will start from 0 and till less than 3
    print("hello",i)
    i+=1 #range itselt increments it so no need of this statement just for explanation

#EX 2
for me in range(1,4):
    print(me)
    me+=1

#EX 3
list=[1,2,3,4]
for i in list:
    print(i) #similar for tuples

#EX 4 
st="laiba"
for i in st:
    print(i)

#also we can add step size:
for i in range(0,11,2): #2 is step size
    print(i)

#lets write table of a given number
num=int(input("Enter the number you want to print the table of: "))
for i in range(11):
    print(num*i)

#factorial of a number
num=int(input("Enter the number you want to print the factorial of: "))
fact=1
for i in range(1,num+1):
    fact=fact*i


print(f"The factorial of number is: {fact}")

#break statements: used to come out of loops it break the loop
num=int(input("Enter the number : "))
for i in range(0,num):
    if(i==33):
        break
    print(i)

#continue statements: skip this iteration
num=int(input("Enter the number : "))
for i in range(0,num):
    if(i==33):
        continue
    print(i)
