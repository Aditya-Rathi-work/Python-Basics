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
full_nameme=first_name+last_name
print(full_nameme) # prints 'JohnDoe'
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

#String Immutability
'''
z="Hello World"
# z[0]='h' # This will raise an error because strings are immutable
print(z)
z="h"+z[1:] # This is the correct way to change the first character
print(z) # prints 'hello World' 
'''

'''Python forces to treat strings as immutable to ensure data integrity and consistency.
 If strings were mutable, changing a string in one part of the program could inadvertently 
 affect other parts of the program that rely on the original string value. 
 This immutability helps prevent bugs and makes code easier to understand and maintain.'''

#______________________________________________________#

# String Methods

s=" Hello World "
print(s.upper()) # prints ' HELLO WORLD '
print(s.lower()) # prints ' hello world '
print(s.strip()) # prints 'Hello World' strips leading and trailing whitespace
print(s.lstrip()) # prints 'Hello World ' strips leading whitespace
print(s.rstrip()) # prints ' Hello World' strips trailing whitespace
print(s.replace("H","h")) # prints ' Hello world '
print(s.split(" ")) # prints ['', 'hello', 'world', '']
print(s.find("World")) # prints 7
print(s.startswith(" hello")) # prints True
print(s.endswith("world ")) # prints True
print(s.count("o")) # prints 2
print(s.capitalize()) # prints ' hello world '
print(s.title()) # prints ' Hello World '
print(s.isalpha()) # prints False
print(s.isdigit()) # prints False
print(s.isspace()) # prints False
print(s.index("W")) # prints 7
print(s.rfind("o")) # prints 8
print(s.zfill(20)) # prints '0000000000 hello world '
print(s.isalpha()) # prints False when string contains non-alphabetic characters
print(s.isdigit()) # prints False when string contains non-digit characters
print(s.isspace()) # prints False when string contains non-space characters
print(s.startswith(" hello")) # prints True
print(s.endswith("world ")) # prints True
print(s.isalnum()) # prints False

#______________________________________________________#

# Escape Characters
# Escape characters are special characters that are used to represent certain whitespace or non-printable characters in a string.
# They are preceded by a backslash (\) to indicate that they have a special meaning.
# Common escape characters include:
# \n - Newline
# \t - Tab
# \\ - Backslash
# \' - Single Quote
# \" - Double Quote
text="Hello\nWorld"
print(text) # prints Hello and World on separate lines
text="Hello\tWorld"
print(text) # prints Hello and World separated by a tab
text="He said, \"Hello World!\""
print(text) # prints He said, "Hello World!"
text='It\'s a beautiful day!'
print(text) # prints It's a beautiful day!
text="This is a backslash: \\"
print(text) # prints This is a backslash: \

#______________________________________________________#

#Formatted Strings (f-strings)]

# Formatted strings, also known as f-strings, are a way to embed expressions inside string literals, using curly braces {}.
# They are prefixed with the letter 'f' or 'F' before the opening quotation mark.
# F-strings provide a concise and convenient way to include variables and expressions within strings.

name="Alice"
age=30
greeting=f"Hello, my name is {name} and I am {age} years old."
print(greeting) # prints 'Hello, my name is Alice and I am 30 years old.'
pi=3.14159
formatted_pi=f"Pi rounded to 2 decimal places is {pi:.2f}"
print(formatted_pi) # prints 'Pi rounded to 2 decimal places is 3.14'
x=1340
y=50
calculation=f"The sum of {x} and {y} is {x+y}"
print(calculation) # prints 'The sum of 1340 and 50 is 1390'

#______________________________________________________#