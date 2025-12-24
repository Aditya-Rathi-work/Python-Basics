#Varibales

#Dynamic Typing
x= 5
y="John"
print(x)
print(y)
x="sally"
print(x)
#value is varibale x is checked during the runtime and changes from int to str

#Naming Rules

#1. Starrt with alphabet or underscore
#2. Cannot start with a number.
#3. Alphabets numberers or underscore only
#4. Case sensitive (age, Age, AGE) are different variables
#5. Keywords cannot be used.

#Reassignment 

# Variables are not storage but rather labels/names that 'point' to a storage location

#Immutable and Mutable

#int str tuples

x=23
y=23
z=23
print(x,y,z)
x=12
print(x,y,z)

#list or dictionaries
myList= ["Apple, Banana,Peach"]
print(myList)
 
my_list = [1, 2, 3]
print(my_list)
my_list.append(4)  # Modifying the list by adding an element
my_list[0] = 0     # Modifying the list by changing an element
print(my_list)     # Output: [0, 2, 3, 4]

#Augmented Arguments

x=6
x+=1
print(x)

#Mutliple Assignment

x,y,z,c=my_list
print(x,y,z,c)

#Built In data type

a = 4           # int
b = 4.5         # float
c = 1j          # complex
d = "Hello"     # string
e = True        # bool          
f = [1, 2, 3]   # list
g = (1, 2, 3)   # tuple 
h = {1: "apple", 2: "banana"}  # dict
i = {1, 2, 3}   # set
j = frozenset({1, 2, 3})  # frozenset
k = bytes(5)    # bytes
l = bytearray(5)  # bytearray
m = memoryview(bytes(5))  # memoryview
n= range(6)  # range
o = {"name": "John", "age": 30, "city": "New York"}  # dict

print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)

#Type

x=10
y=10.00
z=1j

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#Isinstance

# Example 1: Checking a variable's type
x = 5
print(isinstance(x, int))  # Output: True
print(isinstance(x, float)) # Output: False

# Example 2: Checking against multiple types
y = "hello"
print(isinstance(y, (int, str)))  # Output: True (because y is a string)
print(isinstance(y, (int, float))) # Output: False

# Example 3: Using with classes and inheritance
class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()
print(isinstance(my_dog, Dog))    # Output: True
print(isinstance(my_dog, Animal)) # Output: True (because Dog is a subclass of Animal)

#Implicit Conversion

#automatically converts
#no data loss

a=5.93
b=7
print(a+b)

#Explicit Conversion

#user intervenes
#data loss possible

a=12.44
b=int(a)
c=str(a)

print(a,type(a))
print(b,type(b))
print(c,type(c))


#Operators

#arithematic

a=100
b=3
c=456

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulus returns the remainder
print(a**b) #exponentiation i.e raising to the power
print(a//b) #floor division returns value to the nearest integer

#assignment operator

a= 5 # '='
print(a)
a+=3
print(a)
a-=2
print(a)
a*=4
print(a)
print(a)
a/=2
print(a)
a%=2
print(a)
a//=3
print(a)

# Bitwise Operator

a=6 #0110
b=7 #0111
a&=b # '&' bitwise AND operator compares the corresponding bits of two numbers. If both bits are 1, the resulting bit is 1; otherwise, it's 0.
print(a)

a|=b # '|' btiwse OR if either bit is 1 result would be 1 or else 0
print(a)
 
a^=b # '^' bitwise XOR operatorif both bits are same then 0 or else 1
print(a)

print(~b)
# '~' bitwise NOT flips all bits

# Comparison Operator

a=5
b=6

print(a==b) #equals to
print(a!=b) #not equal to
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#chaining
 
print(1<a<10)
print(1<a and a<10)

#Logical Operators

a=10
b=5

print(a<5 and a<20) # 'and' operator returns True if both are ture
print(b<4 or a>5) # 'or' operator returns True if either statement is ture
print(not(b<10 and a>b)) # 'not' operators turns the result

#Identity Operator

x=["apple","banana"]
y=["apple","banana"]
x=z
print(x is z)
print(x is y)
print(y==z)

#Membership Operator

x="Hello World"
y="Hello"
z=["Red","Blue","Green"]

print("H" in x)
print("World"in y)
print("black" not in z)

'''
Do I know when Python converts types automatically? Yes

Do I know why division returns float? Yes, it performs true division, to stay consistent for float inputs, for precision

Do I know the difference between == and is?
== checks for equal values
is checks for location pointed
'''