x =1
y=2.3
z= 1j
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

#integer
# whole number, +ve or -ve number, without decimal of unlimited length
x=1
y=10
z=-2345565
print(x)
print(y)
print(z)

#float
# floating point number, +ve or -ve number, containing one or more decimals
x=1.10
y= -2.5
z=3.14e2
print(x)
print(y)
print(z)
print(type(z))
print(type(x))
print(type(y))

#complex
# complex number, +ve or -ve number, containing 'j' as the imaginary part
x=3+5j
y=5j
z=-2j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#type conversion
x=1    # int
y=2.8  # float
z=1j   # complex

#convert from int to float:
a=float(x)
print(a)

#convert from float to int:
b=int(y)
print(b)

#convert from int to complex:
c=complex(x)
print(c)

print(type(a))
print(type(b))
print(type(c))

# cannot convert complex to another number type

#random number

#python does not have a built-in random number type, but we can import a module to work with random numbers.
import random

print(random.randrange(1, 10))
