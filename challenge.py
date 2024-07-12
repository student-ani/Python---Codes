# 1-
"""name = input("Enter name: ")
age = input("Enter age: ")
address = input("Enter address: ")
print(name)
print(age)
print(address)

# 2-
print("Before conversion")
x = 4
print("x = ",x)
y = 5
print("y = ",y)
temp = x
x = y
y = temp
print("After convrsion")
print("x = ",x)
print("y = ",y)

# 3-
x = 1.23
print(type(x))
y=int(x)
print(type(y))

#4
num = int(input("Enter number: "))
print("it's positive number!") if num>0 else print("it's negative number")

#5
num = int(input("Enter number: "))
print("it's even number") if num%2==0 else print("it's odd number")"""

#6
print("Area Calculator")
print("""Press- 1 for area of Square
Press- 2 for area of rectangle
Press- 3 for area for Circle
Press- 4 for area of triangle""")

choice = int(input("Choose number between 1-4: "))

if choice == 1:
    side = ("Enter one side of square: ")
    area = side*side
    print("your area of square is: ",area)

elif choice == 2:
    len = int(input("Enter Length: "))
    brd = int(input("Enter Breadth: "))

    area = len * brd
    print("area of rectangle is: ",area)

elif choice == 3:
    rad = int(input("Enter radius of circle: "))
    area = 3.14*rad*rad
    print("area of circle is",area)

elif choice == 4:
    base = int(input("Enter base of triangle: "))
    hgt = int(input("Enter height of triangle: "))
    area = 0.5*base*hgt
    print("area of triangle is: ",area)













