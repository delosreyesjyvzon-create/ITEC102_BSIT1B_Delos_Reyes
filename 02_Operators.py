# """ TOPIC 2: OPERATORS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: Arithmetic operators in real use ----------
math, science, english = 88, 92, 79
average = (math + science + english) / 3
print(f"Average: {average:.2f}")

length, width = 12, 5
print("Area :", length * width)
print("Perimeter:", 2 * (length + width))

total_minutes = 135
print(f"{total_minutes} min = {total_minutes // 60} hr {total_minutes % 60} min")
print("2 to the power of 10 =", 2 ** 10)

# ---------- EXAMPLE 2: Assignment operators ----------
x = 10
x += 5      # x = x + 5 -> 15
print("+=", x)
x -= 3      # x = x - 3 -> 12
print("-=", x)
x *= 2      # x = x * 2 -> 24
print("*=", x)
x /= 4      # x = x / 4 -> 6.0
print("/=", x)
x //= 4     # x = x // 4 -> 1.0
print("//=", x)
x = 17
x %= 5      # x = x % 5 -> 2
print("%=", x)
x **= 3     # x = x ** 3 -> 8
print("**=", x)

# ---------- EXAMPLE 3: Comparison operators ----------
a, b = 10, 20
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= 10: {a >= 10}")
print(f"{b} <= 15: {b <= 15}")
print("apple" < "banana")      # strings compare alphabetically



# """ TOPIC 2: OPERATORS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: Logical operators and short-circuiting ----------
age, has_ticket, is_vip = 17, True, False
print(age >= 18 and has_ticket)          # False
print(age >= 18 or is_vip)               # False
print(not is_vip)                        # True

# 'and' / 'or' actually return one of the values, not just True/False
name = ""
print(name or "Guest")                   # empty string is falsy -> "Guest"
print("Ana" and "Welcome")               # both truthy -> last value

def noisy():
    print("noisy() was called")
    return True

print(False and noisy())                 # short-circuit: noisy() never runs
print(True or noisy())                   # short-circuit again

# ---------- EXAMPLE 5: Operator precedence ----------
print(2 + 3 * 4)           # 14 (multiplication first)
print((2 + 3) * 4)         # 20 (parentheses first)
print(2 ** 3 ** 2)         # 512 (** is right-to-left: 2 ** 9)
print(-3 ** 2)             # -9 (** before unary minus)
print(10 - 4 - 2)          # 4 (left to right)
print(not True or True)    # True (not > and > or)
print(5 > 3 and 2 > 1 or False)

# ---------- EXAMPLE 6: Membership and identity operators ----------
text = "Python programming"
print("Python" in text)            # True
print("Java" not in text)          # True
print("o" in "hello")              # True

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)                      # True -> same VALUE
print(a is b)                      # False -> different objects in memory
print(a is c)                      # True -> same object
value = None
print(value is None)               # correct way to check for None



# """ TOPIC 2: OPERATORS - HARD (Examples 7-8) """

# ---------- EXAMPLE 7: Bitwise operators - permission flags ----------
READ, WRITE, EXECUTE = 4, 2, 1       # 100, 010, 001 in binary

permissions = 0
permissions |= READ                  # turn READ on
permissions |= WRITE                 # turn WRITE on
print(f"Permissions: {permissions:03b}")                     # 110

print("Can read? ", bool(permissions & READ))              # True
print("Can execute?", bool(permissions & EXECUTE))           # False

permissions ^= WRITE                 # toggle WRITE (turns it off)
print(f"After toggle: {permissions:03b}")                    # 100

permissions |= EXECUTE
permissions &= ~READ                 # turn READ off using NOT + AND
print(f"Final: {permissions:03b}")                           # 001

print(~5, 5 << 2, 20 >> 2)           # -6, 20, 5

# ---------- EXAMPLE 8: Walrus operator (:=) and compact expressions ----------
# := assigns a value inside an expression
text = "Python operators"
if (n := len(text)) > 10:
    print(f"Text is long ({n} characters)")

total = 0
while (square := total ** 2) < 50:
    print(f"{total} squared = {square}")
    total += 1

score = 76
result = "Pass" if score >= 75 else "Fail"
print(result)
print(10 < score < 100)              # chained comparison