 #DICTIONARY
#We can store key value pairs in disctionary (for example the student and their respective marks,any thing and its corresponting colour ,attribute etc)
MyEatables={"apple":"fruit",
             "tomato":"vegetable",
              "egg" :"dairy"
              }
print(type(MyEatables)) #just to check its type
print(MyEatables["tomato"]) #vegetable is printed

#SOME METHODS:
print(MyEatables.items()) #give the list of all items in dictionary
print(MyEatables.keys()) #gives values of left hand side
print(MyEatables.values()) #gives values of right hand side

#AS DICTIONARY IS MUTABLE SO WE CAN EDIT/UPDATE IT
MyEatables.update({"apple":"dessert","milk":"protein","carrot":"vegetable"})
#As a result the existing items get updated and new ones add (only LHS matters)
print(MyEatables.items())
#how to make empty distionary: 
d={}

#SETS
#how to make empty set: 
e=set()
#Elements cant be repeated in a set also the order is not maintained so to maintain order lists are used

#lets make a mini dictionary
words={"Book":"kitaab",
       "friend":"dost",
       "house":"ghar"}
word=input("Enter word you wanna translate ")#should be in the list
print(words[word])

#user will enter data in dictionary
d={} #empty dictionary
name=input("Enter fruit name")
calories=input("Enter its calories")
d.update({name:calories})
name=input("Enter fruit")
calories=input("Enter its calories")
d.update({name:calories})
print(d)

