x=5
print(type(x))  # Output: <class 'int'>
y="john"    
print(type(y))  # Output: <class 'str'>
#setting data types
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

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
print(type(d))  # Output: <class 'str'>
print(type(e))  # Output: <class 'bool'>
print(type(f))  # Output: <class 'list'>
print(type(g))  # Output: <class 'tuple'>
print(type(h))  # Output: <class 'dict'>    
print(type(i))  # Output: <class 'set'>
print(type(j))  # Output: <class 'frozenset'>       
print(type(k))  # Output: <class 'bytes'>
print(type(l))  # Output: <class 'bytearray'>
print(type(m))  # Output: <class 'memoryview'>

print(n)
print (type(n))  # Output: <class 'range'>
print(list(n)) # Output: [0, 1, 2, 3, 4, 5] converts range to list
print(range(6))  # Output: range(0, 6)

print(type(o))  # Output: <class 'dict'>
print(o)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

#setting data types using constructors
a = int(5)           # int
b = float(5.5)       # float
c = complex(1j)      # complex
d = str("Hello")     # string
e = bool(5)          # bool
f = list((1, 2, 3))   # list
g = tuple((1, 2, 3))  # tuple
h = dict(name="John", age=30, city="New York")  # dict
i = set((1, 2, 3))   # set
j = frozenset((1, 2, 3))  # frozenset
k = bytes(5)         # bytes
l = bytearray(5)     # bytearray
m = memoryview(bytes(5))  # memoryview
n = range(6)         # range

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
print(type(d))  # Output: <class 'str'>
print(type(e))  # Output: <class 'bool'>
print(type(f))  # Output: <class 'list'>
print(type(g))  # Output: <class 'tuple'>
print(type(h))  # Output: <class 'dict'>
print(type(i))  # Output: <class 'set'>
print(type(j))  # Output: <class 'frozenset'>
print(type(k))  # Output: <class 'bytes'>
print(type(l))  # Output: <class 'bytearray'>
print(type(m))  # Output: <class 'memoryview'>
print(type(n))  # Output: <class 'range'>

print(a)  # Output: 5
print(b)  # Output: 5.5
print(c)  # Output: 1j
print(d)  # Output: Hello
print(e)  # Output: True
print(f)  # Output: [1, 2, 3]
print(g)  # Output: (1, 2, 3)
print(h)  # Output: {'name': 'John', 'age': 30,
print(i)  # Output: {1, 2, 3}
print(j)  # Output: frozenset({1, 2, 3})
print(k)  # Output: b'\x00\x00\x00\x00\x00'
print(l)  # Output: bytearray(b'\x00\x00\x00\x00\x00')
print(m)  # Output: <memory at ...>
print(n)  # Output: range(0, 6)
 