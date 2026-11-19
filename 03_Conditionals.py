# """ TOPIC 2: CONDITIONALS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: Even or odd ----------
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# ---------- EXAMPLE 2: Positive, negative, or zero ----------
n = -3
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# ---------- EXAMPLE 3: Voting eligibility ----------
age = 17
if age >= 18:
    print("You can vote.")
else:
    print(f"You need to wait {18 - age} more year(s) to vote.")


# """ TOPIC 2: CONDITIONALS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: Grade classifier (if / elif / else ladder) ----------
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} -> Grade {grade}")

# ---------- EXAMPLE 5: Leap year checker ----------
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# ---------- EXAMPLE 6: Ternary expression and chained comparison ----------
temp = 28
status = "Hot" if temp > 30 else "Warm" if temp >= 20 else "Cold"
print(f"{temp} C is {status}")

age = 25
print("Young adult" if 18 <= age <= 30 else "Not a young adult")


# """ TOPIC 2: CONDITIONALS - HARD (Examples 7-9) """

# ---------- EXAMPLE 7: Login check with nested conditions ----------
saved_user, saved_pass = "admin", "py123"
username, password = "admin", "wrong"
attempts = 2

if username == saved_user:
    if password == saved_pass:
        print("Login successful!")
    elif attempts >= 3:
        print("Account locked.")
    else:
        print(f"Wrong password. {3 - attempts} attempt(s) left.")
else:
    print("Unknown user.")

# ---------- EXAMPLE 8: match-case (structural pattern matching, Python 3.10+) ----------
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit" | "exit":  # several patterns in one case
        print("Stopping...")
    case _:  # default case
        print("Unknown command")

value = -5
match value:
    case 0:
        print("Zero")
    case n if n > 0:  # guard condition
        print("Positive")
    case n if n < 0:
        print("Negative")

# ---------- EXAMPLE 9: Triangle classifier with validation ----------
a, b, c = 3, 4, 5
if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
else:
    if a == b == c:
        kind = "equilateral"
    elif a == b or b == c or a == c:
        kind = "isosceles"
    else:
        kind = "scalene"
    longest = max(a, b, c)
    # Right triangle test: a^2 + b^2 + c^2 == 2 * (longest side)^2
    right = " and right-angled" if a**2 + b**2 + c**2 == 2 * longest**2 else ""
    print(f"Valid triangle: {kind}{right}")
