#  Python Keywords 

# 1️⃣ Boolean Keywords
x = True
y = False
z = None  # Means "no value"

print(x, y, z)  # Output: True False None
print(type(x))  # Output: <class 'bool'>

# 2️⃣ Conditional Keywords
age = 18
if age > 18:
    print("You can vote.")
elif age == 18:
    print("You are eligible to vote this year!")
else:
    print("You cannot vote yet.")

# 3️⃣ Looping Keywords
for i in range(3):
    print("For loop iteration:", i)

count = 0
while count < 3:
    print("While loop iteration:", count)
    count += 1

# 4️⃣ Exception Handling Keywords
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")

# 5️⃣ Function and Return Keywords
def greet(name):
    return f"Hello, {name}!"

print(greet("Ali"))

# 6️⃣ Class and Object Keywords
class Person:
    def _init_(self, name):
        self.name = name

p1 = Person("Ahmed")
print("Person's name is:", p1.name)

# 7️⃣ Import Keywords
import math
print("Square root of 16:", math.sqrt(16))

# 8️⃣ Global and Nonlocal Keywords
global_var = "I am global"

def outer():
    local_var = "I am local"

    def inner():
        nonlocal local_var
        local_var = "Modified in inner function"
        print(local_var)

    inner()

outer()

# 9️⃣ Pass, Break, Continue Keywords
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    if i == 4:
        break  # Exit loop
    print("Loop value:", i)

# 1️⃣0️⃣ Lambda Function
square = lambda x: x * x
print("Square of 5:", square(5))