# """ TOPIC 1: PYTHON BASICS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: Hello World and print() options ----------
print("Hello, World!")
print("Python", "is", "fun", sep="-")  # sep = separator between items
print("Loading", end="...")  # end = what is printed at the end
print("done!")

# ---------- EXAMPLE 2: Variables and data types ----------
name = "Maria"  # str (text)
age = 19  # int (whole number)
height = 1.58  # float (decimal number)
is_student = True  # bool (True / False)

print(name, "->", type(name))
print(age, "->", type(age))
print(height, "->", type(height))
print(is_student, "->", type(is_student))

# ---------- EXAMPLE 3: Arithmetic operators ----------
a, b = 17, 5
print("Add:", a + b)  # 22
print("Subtract:", a - b)  # 12
print("Multiply:", a * b)  # 85
print("Divide:", a / b)  # 3.4 (always a float)
print("Floor divide:", a // b)  # 3 (drops the decimal)
print("Modulo:", a % b)  # 2 (remainder)
print("Power:", a**2)  # 289



# """ TOPIC 1: PYTHON BASICS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: User input and type conversion ----------
# input() always returns a string, so convert it with int() or float().
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hi {name}! Next year you will be {age + 1} years old.")

# ---------- EXAMPLE 5: f-string formatting ----------
price = 1234.5678
print(f"Two decimals : {price:.2f}")       # 1234.57
print(f"With commas : {price:,.2f}")      # 1,234.57
print(f"Left aligned : |{'left':<10}|")
print(f"Right aligned: |{'right':>10}|")
print(f"Centered : |{'mid':^10}|")
print(f"Percentage : {0.256:.1%}")       # 25.6%
print(f"Zero padded : {7:03d}")           # 007

# ---------- EXAMPLE 6: Comparison and logical operators ----------
age = 20
has_id = True
print(age >= 18)                    # True
print(age == 21)                    # False
print(age >= 18 and has_id)         # True -> both must be True
print(age < 18 or has_id)           # True -> at least one is True
print(not has_id)                   # False -> reverses the value
print(18 <= age <= 25)              # True -> chained comparison



# """ TOPIC 1: PYTHON BASICS - HARD (Examples 7-9) """

# ---------- EXAMPLE 7: Convert seconds to hours:minutes:seconds ----------
total_seconds = 98765
hours, remainder = divmod(total_seconds, 3600)   # divmod returns (quotient, remainder)
minutes, seconds = divmod(remainder, 60)
print(f"{total_seconds} seconds = {hours:02d}:{minutes:02d}:{seconds:02d}")

# ---------- EXAMPLE 8: Swapping variables and bitwise operators ----------
x, y = 5, 9
x, y = y, x                       # swap without a temporary variable
print("After swap:", x, y)

a, b = 12, 10                     # 1100 and 1010 in binary
print("a & b =", a & b)          # AND -> 8
print("a | b =", a | b)          # OR -> 14
print("a ^ b =", a ^ b)          # XOR -> 6
print("a << 1 =", a << 1)         # shift left (multiply by 2) -> 24
print("a >> 1 =", a >> 1)         # shift right (divide by 2) -> 6

n = 15
print(f"{n} is", "odd" if n & 1 else "even")   # last bit tells odd/even

# ---------- EXAMPLE 9: Mini project - receipt calculator ----------
item1_name, item1_price, item1_qty = "Notebook", 45.50, 3
item2_name, item2_price, item2_qty = "Ballpen", 12.00, 10
item3_name, item3_price, item3_qty = "Folder", 8.75, 4

line1 = item1_price * item1_qty
line2 = item2_price * item2_qty
line3 = item3_price * item3_qty

subtotal = line1 + line2 + line3
discount = subtotal * 0.10 if subtotal > 250 else 0
vat = (subtotal - discount) * 0.12
total = subtotal - discount + vat
payment = 500
change = payment - total

print("=" * 34)
print(f"{'RECEIPT':^34}")
print("=" * 34)
print(f"{item1_name:<12}{item1_qty:>3} x {item1_price:>7.2f} = {line1:>7.2f}")
print(f"{item2_name:<12}{item2_qty:>3} x {item2_price:>7.2f} = {line2:>7.2f}")
print(f"{item3_name:<12}{item3_qty:>3} x {item3_price:>7.2f} = {line3:>7.2f}")
print("-" * 34)
print(f"{'Subtotal:':<22}{subtotal:>12,.2f}")
print(f"{'Discount (10%):':<22}{-discount:>12,.2f}")
print(f"{'VAT (12%):':<22}{vat:>12,.2f}")
print(f"{'TOTAL:':<22}{total:>12,.2f}")
print(f"{'Cash:':<22}{payment:>12,.2f}")
print(f"{'Change:':<22}{change:>12,.2f}")