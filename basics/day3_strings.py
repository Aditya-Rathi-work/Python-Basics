#STRINGS
 
# Creating Strings

# A string is a sequence of characters enclosed within single quotes(' ') or double quotes(" ")
# Strings are immutable, meaning once created, their content cannot be changed.
# Strings can contain letters, numbers, symbols, and spaces.
# Strings can be created using the str() constructor or by directly assigning a value to a variable.
# Examples:
a='Hello'
b="World"
c=str("Hello World")
print(a)
print(b)
print(c)

#______________________________________________________#

# Concatenation and Repetition
first_name="John"
last_name="Doe"
full_name=first_name+" "+last_name
print(full_name) # prints 'John Doe'
greeting="Hello! "*3
print(greeting) # prints 'Hello! Hello! Hello! '

#______________________________________________________#

# Accessing Characters in a String
x=str("Hello World")
print(x)
print(x[0]) # prints first character
print(x[10]) # prints last character
 
#______________________________________________________#

#Indexing in Strings

a="Hello World"
print(a[0]) # prints 'H'
print(a[4]) # prints 'o'
print(a[-1]) # prints 'd'
print(a[-5]) # prints 'W'

#______________________________________________________#

# Extracting Characters

y="This is a String"
print(y[0:3])
print(y[-1:-3]) #fails becasue negative indexing goes right to left
print(y[-3:]) #prints 'ing'
print(y[0:10:2]) # prints every second character from index 0 to 9
print(y[:5]) # prints first 5 characters
print(y[5:]) # prints from index 5 to end
print(y[:]) # prints whole string
print(y[::-1]) # prints string in reverse order the same as y[len(y)-1::-1]
print(len(y)) # prints length of string
print(y[len(y)-1::-1]) # prints string in reverse order
print(y[::3]) # prints every third character

