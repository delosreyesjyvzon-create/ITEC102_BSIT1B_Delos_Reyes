# """ TOPIC 5: STRINGS - EASY (Examples 1-3) """

# ---------- EXAMPLE 1: Indexing and slicing ----------
s = "Python Programming"
print(s[0])        # P
print(s[-1])       # g
print(s[0:6])      # Python
print(s[7:])       # Programming
print(s[::-1])     # reversed
print(s[::2])      # every 2nd character

# ---------- EXAMPLE 2: Changing case ----------
text = "hello wORLD"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# ---------- EXAMPLE 3: Length, concatenation, repetition, membership ----------
first, last = "Juan", "Dela Cruz"
full = first + " " + last
print(full, "has", len(full), "characters")
print("-" * 20)
print("Dela" in full)        # True
print("xyz" not in full)     # True



# """ TOPIC 5: STRINGS - INTERMEDIATE (Examples 4-6) """

# ---------- EXAMPLE 4: strip, replace, find, count ----------
text = " Hello, World! Hello, Python! "
print(repr(text.strip()))                    # removes outer spaces
print(text.replace("Hello", "Hi"))
print(text.find("World"))                    # index, or -1 if not found
print(text.count("Hello"))
print(text.strip().startswith("Hello"))
print(text.strip().endswith("!"))

# ---------- EXAMPLE 5: split and join ----------
sentence = "the quick brown fox"
words = sentence.split()                     # split on whitespace
print(words)
print("-".join(words))                       # join with a separator
print(" ".join(w.capitalize() for w in words))

line = "Ana,19,BSIT"
name, age, course = line.split(",")
print(name, age, course)

# ---------- EXAMPLE 6: Palindrome checker ----------
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))                              # True
print(is_palindrome("A man, a plan, a canal: Panama"))     # True
print(is_palindrome("python"))                             # False



# """ TOPIC 5: STRINGS - HARD (Examples 7-9) """

# ---------- EXAMPLE 7: Caesar cipher ----------
def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch                     # keep spaces and symbols
    return result

secret = caesar("Hello, World!", 3)
print("Encrypted:", secret)                  # Khoor, Zruog!
print("Decrypted:", caesar(secret, -3))      # Hello, World!

# ---------- EXAMPLE 8: Anagram checker ----------
def is_anagram(a, b):
    clean_a = "".join(ch.lower() for ch in a if ch.isalpha())
    clean_b = "".join(ch.lower() for ch in b if ch.isalpha())
    return sorted(clean_a) == sorted(clean_b)

print(is_anagram("Listen", "Silent"))                  # True
print(is_anagram("Dormitory", "Dirty room"))           # True
print(is_anagram("Hello", "World"))                    # False

# ---------- EXAMPLE 9: Password strength checker ----------
def check_password(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if any(ch.islower() for ch in pw):
        score += 1
    if any(ch.isupper() for ch in pw):
        score += 1
    if any(ch.isdigit() for ch in pw):
        score += 1
    if any(not ch.isalnum() for ch in pw):
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"

for pw in ("abc", "password1", "Passw0rd", "P@ssw0rd!2026"):
    print(f"{pw:<15} -> {check_password(pw)}")