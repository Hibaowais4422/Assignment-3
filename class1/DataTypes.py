#  Python Data Types 

# 1️⃣ Numeric Data Types
x = 10  # Integer type
y = 3.14  # Floating point type
z = 2 + 3j  # Complex number type

print("Numeric Data Types:", x, y, z)
print(type(x), type(y), type(z))  # Output: <class 'int'> <class 'float'> <class 'complex'>

# 2️⃣ Boolean Data Type
a = True
b = False
c = None  # Means "no value"

print("Boolean Values:", a, b, c)
print(type(a), type(b), type(c))  # Output: <class 'bool'> <class 'bool'> <class 'NoneType'>

# 3️⃣ Sequence Data Types
string_value = "Hello, Python!"  # String type
list_value = [1, 2, 3, 4, 5]  # List type (Mutable)
tuple_value = (10, 20, 30)  # Tuple type (Immutable)
range_value = range(5)  # Range type

print("String:", string_value)
print("List:", list_value)
print("Tuple:", tuple_value)
print("Range:", list(range_value))  # Converting range to list for display

# 4️⃣ Set Data Types
set_value = {1, 2, 3, 4, 5}  # Set type (Unique values, unordered)
frozenset_value = frozenset([1, 2, 3, 4, 5])  # Immutable set

print("Set:", set_value)
print("Frozenset:", frozenset_value)

# 5️⃣ Mapping Data Type (Dictionary)
dict_value = {"name": "Ali", "age": 22, "city": "Karachi"}  # Dictionary type (Key-Value pairs)

print("Dictionary:", dict_value)

# 6️⃣ Binary Data Types
bytes_value = b"Python"  # Bytes type
bytearray_value = bytearray([65, 66, 67])  # Bytearray type (Mutable)
memoryview_value = memoryview(bytes([65, 66, 67]))  # Memoryview type

print("Bytes:", bytes_value)
print("Bytearray:", bytearray_value)
print("Memoryview:", list(memoryview_value))  # Converting to list for readability