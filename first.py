"""print("1- Hello world")

#----------*in multiple lines print*--------(Comment by "#")
print('''2- Hello 
      world''')
print("3- hello friends \n this is my first python program")
#multiple lines comments written in triple quotes

# variables-
a = "I'm a data scientist"
print(a)

# user inputs-
name = input("Enter your name: ")   #if enter any name or word the variable automatic store in the string.
print (name)
age  = int(input("Enter age: "))
print(age)
sum = eval(input("Enter expression: "))
print(sum)

#type conversion(1.implicit- by compiler)
b = 456
c = 2.31
d =b +c
print(d)
print(type(d))

#Explicit- (by user)
x ="250"
y =52
x=int(x)
print(x)
z = x+y
print(z)

#print binary
print(bin(8))
a = 4
b = 6
print(a & b)

#membership operator
a = "Aniket"
print ("i" in a)

#only if condition
marks = 70
if marks >=85:
    print('you win cash')

print("Thank you")    

#if-else
marks = int(input("Enter marks: "))
if marks>=60:
    print("Ist Devision")
else:
    print("IInd Devision")
print("Congratulations") 

#else-elif
marks = int(input("Enter marks: "))
if marks >= 85:
    print('Go for trip')
elif marks >= 70:
    print("1 week holiday")
else:
    print("Still study")

#shorthand if statement
marks = int(input("Enter marks: "))
if marks >= 85: print("Great Job!")

#shorthand if-else statement
marks = int(input("Enter marks: "))
print("Great Job!") if marks>=85 else print("more hardwork")"""
