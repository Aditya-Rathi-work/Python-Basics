#single and double quotes
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
#triple quotes for multi-line strings
triple_quote_string = """This is a multi-line string.It can span multiple lines
and include 'single' and "double" quotes."""
print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)
 
 #qoute inside quote
single_inside_double = "He said, 'Hello!'"
double_inside_single = 'She replied, "Hi!"'
print(single_inside_double)
print(double_inside_single)

#strings are arrays
a="Hello, World!"
print(a[1])  # Output: e    
print(a[0])  # Output: H
print(a[7])  # Output: W

#looping through a string
for a in "banana":
    print(a) 

#string length
# use len() function to get length of string
# len() is a built-in function in Python that returns the number of characters in a string.
# It counts all characters, including letters, numbers, spaces, and special characters.
# Example:
a = "Hello, World!" 
print(len(a))

#Check string
txt = " The best thing in life are free"
print("free" in txt)

#using it in an "if" statement

if "free" in txt:
   print("yes,  'free' is present")

if "expensive"  not in txt:
    print("No, 'expensive' is not in txt")

#Slicing

#return a raneg of characters using syntax slice

b="Hello, World!"
print(b[2:5])
#5 not included

#slice from the start
print(b[:5])
#5 not included

#slice till the end
print(b[2:])

#Negative  Indexing
print(b[-5:-2]) 