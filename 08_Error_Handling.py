# """ TOPIC 7: ERROR HANDLING - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: try / except ----------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# ---------- EXAMPLE 2: Catching ValueError ----------
try:
    number = int("abc")
except ValueError:
    print("That is not a valid number.")

# ---------- EXAMPLE 3: try / except / else / finally ----------
try:
    value = int("42")
except ValueError:
    print("Invalid number")
else:                                   # runs only if NO error happened
    print("Converted successfully:", value)
finally:                                # ALWAYS runs
    print("Done checking.")



# """ TOPIC 7: ERROR HANDLING - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: Multiple except blocks ----------
def divide_text(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Error: inputs must be numbers"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: wrong input type"

print(divide_text("10", "2"))
print(divide_text("ten", "2"))
print(divide_text("10", "0"))
print(divide_text(None, "2"))

# ---------- EXAMPLE 5: Raising your own errors ----------
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistic")
    return age

for test_age in (25, -5, 200):
    try:
        print("Valid age:", set_age(test_age))
    except ValueError as error:
        print("Rejected:", error)

# ---------- EXAMPLE 6: Handling missing files ----------
try:
    with open("this_file_does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as error:                 # catch-all (use it last)
    print("Unexpected error:", error)



# """ TOPIC 7: ERROR HANDLING - HARD (Examples 7-9) """

# ---------- EXAMPLE 7: Input validation with retries ----------
# In a real program you would use input(); these are simulated attempts.
attempts = ("abc", "-4", "150", "25")
for attempt_number, raw in enumerate(attempts, start=1):
    try:
        age = int(raw)
        if not 0 <= age <= 120:
            raise ValueError("age must be between 0 and 120")
    except ValueError as error:
        print(f"Attempt {attempt_number}: '{raw}' rejected ({error})")
    else:
        print(f"Attempt {attempt_number}: accepted age {age}")
        break

# ---------- EXAMPLE 8: Validation, assert, and exception chaining ----------
def withdraw(balance, amount):
    assert balance >= 0, "Balance must never be negative"
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds (balance: {balance})")
    return balance - amount

for amount in (200, 5000, -10):
    try:
        print("New balance:", withdraw(1000, amount))
    except ValueError as error:
        print("Transaction failed:", error)

def parse_price(text):
    try:
        return float(text)
    except ValueError as error:
        raise RuntimeError(f"Cannot read price '{text}'") from error   # chaining

try:
    parse_price("12.5php")
except RuntimeError as error:
    print(error, "| caused by:", repr(error.__cause__))

# ---------- EXAMPLE 9: Safe calculator ----------
def calculate(a, op, b):
    try:
        a, b = float(a), float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            raise ValueError(f"Unknown operator '{op}'")
    except ZeroDivisionError:
        return "Math error: division by zero"
    except ValueError as error:
        return f"Input error: {error}"
    finally:
        print(" (calculation attempted)")

print(calculate(10, "+", 5))
print(calculate(10, "/", 0))
print(calculate("x", "*", 3))
print(calculate(4, "%", 2))