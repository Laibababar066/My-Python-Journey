#function definition
def myFirstFunction(): #user defined function
    print("Hello my first function is called")
myFirstFunction() #function call

#there are two types: 1. built_in functions  2. user defined functions

#lets try functions with parameters
def greetings(name):
    print("Good Morning, "+name)

greetings("Laiba Babar")

#using return to store the value of function in a variable later
def calculateAvg():
    num = int(input("Enter the number of marks: "))
    sum_marks = 0
    for i in range(num):
        marks = int(input(f"Enter the marks of student {i+1}: "))
        sum_marks += marks
    average = sum_marks / num
    return average

a = calculateAvg()
print(f"The average is: {a}")

#default parameter
def greetings2(name,ending="Thankyou"):
    print(f"hiii {name } , {ending}")

greetings2("laiba")
greetings2("zara","byee") #bye will print

#............RECURSION.................
#It is a process in which fuction calls itself
def factorial(n):
    if(n==1 or n==0):
        return 1 #Base case
    return n*factorial(n-1)
num=int(input("Enter a number to calculate its factorial "))
print(f"The factorial is: {factorial(num)}")

#celcius to fahrenheit
def conversion():
    celcius=int(input("Enter temp in F "))  #formula= fahrenheit = (9/5) * celsius + 32
    fahrenheit=(9/5)*celcius+32
    print(f"the temp in fahrenheit is: {fahrenheit}")
conversion()





