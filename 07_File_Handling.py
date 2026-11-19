# """ TOPIC 6: FILE HANDLING - EASY (Examples 1-3) Files created here go inside an 'output' folder next to this script. """
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "hello.txt")

# ---------- EXAMPLE 1: Writing a file ("w" overwrites) ----------
with open(path, "w") as f:
    f.write("Hello, file!\n")
    f.write("This is the second line.\n")
print("File written.")

# ---------- EXAMPLE 2: Reading a file ----------
with open(path, "r") as f:
    content = f.read()
print(content)

# ---------- EXAMPLE 3: Appending to a file ("a" adds to the end) ----------
with open(path, "a") as f:
    f.write("This line was appended.\n")

with open(path) as f:                 # "r" is the default mode
    print(f.read())



# """ TOPIC 6: FILE HANDLING - INTERMEDIATE (Examples 4-6) """
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "poem.txt")

with open(path, "w") as f:
    f.write("Roses are red\nViolets are blue\nPython is great\nAnd so are you\n")

# ---------- EXAMPLE 4: Reading line by line ----------
with open(path) as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.strip()}")

# ---------- EXAMPLE 5: Counting lines, words, and characters ----------
with open(path) as f:
    text = f.read()
print("Lines :", len(text.splitlines()))
print("Words :", len(text.split()))
print("Characters:", len(text))

# ---------- EXAMPLE 6: Checking, renaming, and deleting files ----------
print("Exists?", os.path.exists(path))
print("Size :", os.path.getsize(path), "bytes")

new_path = os.path.join(OUT, "poem_renamed.txt")
os.rename(path, new_path)
print("Renamed. Old exists?", os.path.exists(path))

os.remove(new_path)
print("Deleted. New exists?", os.path.exists(new_path))



# """ TOPIC 6: FILE HANDLING - HARD (Examples 7-9) """
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT, exist_ok=True)

# ---------- EXAMPLE 7: Writing and parsing a CSV-style file by hand ----------
grades_path = os.path.join(OUT, "grades.csv")
with open(grades_path, "w") as f:
    f.write("name,math,science,english\n")
    f.write("Ana,90,85,88\n")
    f.write("Ben,75,80,70\n")
    f.write("Cara,95,92,98\n")

with open(grades_path) as f:
    next(f)                                    # skip the header line
    for line in f:
        name, math, science, english = line.strip().split(",")
        average = (int(math) + int(science) + int(english)) / 3
        print(f"{name:<6} average = {average:.2f}")

# ---------- EXAMPLE 8: Simple log analyzer ----------
log_path = os.path.join(OUT, "app.log")
with open(log_path, "w") as f:
    f.write("INFO Server started\n")
    f.write("ERROR Database connection failed\n")
    f.write("INFO User logged in\n")
    f.write("ERROR Timeout while loading page\n")
    f.write("WARN Disk almost full\n")

errors = 0
with open(log_path) as f:
    for line in f:
        if line.startswith("ERROR"):
            errors += 1
            print("Found:", line.strip())
print("Total errors:", errors)

# ---------- EXAMPLE 9: Persistent to-do list stored in a file ----------
todo_path = os.path.join(OUT, "todo.txt")

def save_all(tasks):
    with open(todo_path, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_all():
    if not os.path.exists(todo_path):
        return []
    with open(todo_path) as f:
        return [line.strip() for line in f]

def add_task(task):
    tasks = load_all()
    tasks.append("[ ] " + task)
    save_all(tasks)

def complete_task(number):
    tasks = load_all()
    tasks[number - 1] = tasks[number - 1].replace("[ ]", "[x]", 1)
    save_all(tasks)

def show_tasks():
    for i, task in enumerate(load_all(), start=1):
        print(f"{i}. {task}")

if os.path.exists(todo_path):
    os.remove(todo_path)                       # start fresh for the demo
add_task("Finish Python notes")
add_task("Record video")
add_task("Upload to GitHub")
complete_task(1)
show_tasks()