#Lists

#Lists are used to store multiple items in a single variable.
#Lists are ordered, changeable (mutable), and allow duplicate values.
#Lists are created using square brackets [] and items are separated by commas.
#Examples:

my_list = [1, 2, 3, "Hello", 4.5, True]
print(my_list)
print(type(my_list))
print(len(my_list))  # prints the number of items in the list 

#_______________________________________________________#

#The List Constructor
#Lists can also be created using the list() constructor.
#Examples:
my_list2 = list((1, 2, 3, "World", 5.6, False))
print(my_list2)

#Accessing List Items

print(my_list[0])  # prints first item
print(my_list[3])  # prints fourth item
print(my_list[-1]) # prints last item
print(my_list[-3]) # prints third last item
print(my_list[1:4]) # prints items from index 1 to 3
print(my_list[:3])  # prints first three items

my_list3=['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
print(my_list3[2:5]) # prints items from index 2 to 4
print(my_list3[::2]) # prints every second item
print(my_list3[::-1]) # prints the list in reverse order
print(my_list3[len(my_list3)-1::-1]) # prints the list in reverse order

if 'banana' in my_list3:
    print("Yes, 'banana' is in the list")
    
#_______________________________________________________#

#Modifying List Items

my_list3[1] = 'blueberry'  # changing the second item
print(my_list3)

my_list3[2:4] = ['coconut', 'dragonfruit']  # changing items from index 2 to 3
print(my_list3)

my_list3.insert(2, 'blackberry')  # inserting 'blackberry' at index 2
print(my_list3)

my_list3.append('honeydew')  # adding 'honeydew' at the end
print(my_list3)

my_list3.extend(['kiwi', 'lemon'])  # adding multiple items at the end
print(my_list3)

thislist=['andy', 'bob', 'charlie']
thislist[1:3]=['randy']
print(thislist)

#diiference between append and extend ad insert

list1=['a','b','c']
print(list1)

list1.append('de')
print(list1)  # ['a', 'b', 'c', 'de']
print(len(list1))

list1.insert(2,'ef')
print(list1)  
print(list1[1:3])  # ['b', 'ef']

list1.extend('de')
print(list1)  # ['a', 'b', 'c', 'd', 'e']
print(len(list1))

str="xyz"
lst2=["xyz"]
list1.extend("xyz")
list1.append(str)
list1.extend(lst2)
print(list1)  # ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
# extend adds each element of the iterable individually to the end of the list

#_______________________________________________________#

#Removing List Items

list3=['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
list3.remove('date')  # removes 'date'
print(list3)

#return removes the first instance of the specified value

list3.pop()  # removes the last item
print(list3)
list3.pop(1)  # removes item at index 1
print(list3)