# """ TOPIC 4: FUNCTIONS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: Defining and calling a function ----------
def greet(name):
    print(f"Hello, {name}!")

greet("Ana")
greet("Ben")

# ---------- EXAMPLE 2: Return values ----------
def area_of_circle(radius):
    return 3.14159 * radius ** 2

area = area_of_circle(5)
print(f"Area = {area:.2f}")

def is_even(n):
    return n % 2 == 0          # returns True or False

print(is_even(10), is_even(7))

# ---------- EXAMPLE 3: Default and keyword arguments ----------
def greet_with(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_with("Carlo"))                       # uses the default
print(greet_with("Carlo", "Good morning"))       # overrides the default
print(greet_with(greeting="Hi", name="Dina"))    # keyword arguments, any order



# """ TOPIC 4: FUNCTIONS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: *args and **kwargs ----------
def total(*numbers):                 # any number of positional arguments
    return sum(numbers)

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))

def show_profile(**info):            # any number of keyword arguments
    for key, value in info.items():
        print(f"{key}: {value}")

show_profile(name="Eli", age=20, course="BSIT")

# ---------- EXAMPLE 5: Variable scope (local vs global) ----------
counter = 0                          # global variable

def add_local():
    counter = 100                    # a NEW local variable, global is untouched
    return counter

def add_global():
    global counter                   # tell Python to use the global one
    counter += 1

add_local()
print("After add_local():", counter)    # still 0
add_global()
add_global()
print("After add_global() x2:", counter)  # 2

# ---------- EXAMPLE 6: Lambda, map, and filter ----------
square = lambda x: x * x             # small one-line anonymous function
print(square(9))

numbers = (1, 2, 3, 4, 5, 6)
print(list(map(lambda x: x * 2, numbers)))          # apply to every item
print(list(filter(lambda x: x % 2 == 0, numbers)))  # keep items that pass

words = ("banana", "kiwi", "apple", "fig")
print(sorted(words, key=lambda w: len(w)))          # sort by length



# """ TOPIC 4: FUNCTIONS - HARD (Examples 7-9) """

import time
from functools import wraps

# ---------- EXAMPLE 7: Recursion ----------
def factorial(n):
    if n <= 1:                       # base case
        return 1
    return n * factorial(n - 1)      # recursive case

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def reverse(text):
    return text if len(text) <= 1 else reverse(text[1:]) + text[0]

print(factorial(6))          # 720
print(fibonacci(10))         # 55
print(gcd(48, 18))           # 6
print(reverse("python"))     # nohtyp

# ---------- EXAMPLE 8: Closures (a function that remembers) ----------
def make_multiplier(factor):
    def multiply(x):
        return x * factor            # 'factor' is remembered from outside
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))        # 20 30

def make_counter():
    count = 0
    def increment():
        nonlocal count               # modify the enclosing variable
        count += 1
        return count
    return increment

counter = make_counter()
print(counter(), counter(), counter())   # 1 2 3

# ---------- EXAMPLE 9: Decorators ----------
def timer(function):
    @wraps(function) # keeps the original function name
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {function.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer # same as: slow_sum = timer(slow_sum)
def slow_sum(n):
    time.sleep(0.2)
    return sum(range(n + 1))

print(slow_sum(1000))