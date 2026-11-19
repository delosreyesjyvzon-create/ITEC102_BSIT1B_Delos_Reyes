# """ TOPIC 3: LOOPS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: for loop with range() ----------
for i in range(1, 6):
    print(i, end=" ")
print()
for i in range(0, 11, 2):     # step of 2
    print(i, end=" ")
print()
for i in range(5, 0, -1):     # countdown
    print(i, end=" ")
print("Liftoff!")

# ---------- EXAMPLE 2: while loop - sum of 1 to n ----------
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of 1 to {n} = {total}")

# ---------- EXAMPLE 3: Multiplication table ----------
num = 7
for i in range(1, 11):
    print(f"{num} x {i:>2} = {num * i}")



# """ TOPIC 3: LOOPS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: Factorial using a loop ----------
n = 6
result = 1
for i in range(2, n + 1):
    result *= i
print(f"{n}! = {result}")

# ---------- EXAMPLE 5: break and continue ----------
# break: stop the loop completely
for num in range(1, 100):
    if num % 5 == 0 and num % 7 == 0:
        print("First multiple of both 5 and 7:", num)
        break

# continue: skip the current round
for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(num, end=" ")
print()

# ---------- EXAMPLE 6: Nested loops - patterns ----------
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

print()
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)       # pyramidv



# """ TOPIC 3: LOOPS - HARD (Examples 7-9) """

# ---------- EXAMPLE 7: Prime numbers using for-else ----------
for n in range(2, 51):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            break                 # found a divisor -> not prime
    else:                         # runs only if the inner loop did NOT break
        print(n, end=" ")
print()

# ---------- EXAMPLE 8: Fibonacci sequence ----------
a, b = 0, 1
for _ in range(15):
    print(a, end=" ")
    a, b = b, a + b
print()

# ---------- EXAMPLE 9: Number guessing game (binary search) ----------
secret = 73
low, high = 1, 100
attempts = 0
while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"Attempt {attempts}: guess {guess}")
    if guess == secret:
        print(f"Found {secret} in {attempts} attempts!")
        break
    elif guess < secret:
        print(" Too low")
        low = guess + 1
    else:
        print(" Too high")
        high = guess - 1