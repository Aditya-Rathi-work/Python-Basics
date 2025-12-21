fruits = ["apple", "banana", "cherry"] 
x,y,z = fruits
print(x)  # Output: apple
print(y)  # Output: banana
print(z)  # Output: cherry
x =5 # Assigning integer value to x
y ="john" # Assigning string value to y
print(x)  # Output: 5
print(y)  # Output: john
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3 
z = float(3)  # z will be 3.0
print(x)  # Output: '3' 
print(y)  # Output: 3
print(z)  # Output: 3.0
#doube and single quotes
x="john "
print(x)  # Output: john
x='john'
print(x)  # Output: john
#case sensitive
a = 4
A = "Sally"
print(a)  # Output: 4   
print(A)  # Output: Sally
#multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Output: Orange
print(y)  # Output: Banana  
print(z)  # Output: Cherry
#variable naming rules
#1. A variable name must start with a letter or the underscore character
#2. A variable name cannot start with a number
#3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#4. Variable names are case-sensitive (age, Age and AGE are three different variables)
#5. Variable names cannot be the same as reserved words/keywords in Python (like print, for, if, etc.)
#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
myvar2 = "John"
#illegal variable names 
#2myvar = "John"  # starts with a number
#my-var = "John"  # contains a hyphen
#my var = "John"  # contains a space
#assign mutliple values to multiple variables
a, b, c = "Orange", "Banana", "Cherry"
print(a)  # Output: Orange
print(b)  # Output: Banana
print(c)  # Output: Cherry
#assign the same value to multiple variables 
x = y = z = "Orange"
print(x,y,z)
print(x+y+z)  # Output: OrangeOrangeOrange
#output variable
x = "awesome"
print("Python is " + x)  # Output: Python is awesome
print("Python is {}".format(x))  # Output: Python is awesome
print(f"Python is {x}")  # Output: Python is awesome    
x= 5
y='john'
#print(x+y)  # This will raise an error

#local variable global variable
x= "awesome" #global variable
def myFunc():
    x="fantastic"
    print("Python is " + x)  # Output: Python is fantastic

myFunc()
print("Python is " + x)  # Output: Python is awesome


#global keyword
x = "awesome"
def myFunc():
    global x
    x = "fantastic"
    print("Python is " + x)  # Output: Python is fantastic
myFunc()
print("Python is " + x)  # Output: Python is fantastic