import json
import random
import time
from pathlib import Path  # only used to find this script's folder

FOLDER = Path(__file__).resolve().parent
QUESTIONS_FILE = FOLDER / "question.json"
SCORES_FILE = FOLDER / "high_scores.json"
POINTS, BONUS, FAST = 10, 5, 5  # points per answer, bonus points, "fast" = 5 seconds


def load_scores():
    if SCORES_FILE.exists():
        with open(SCORES_FILE) as f:
            return json.load(f)  # json: file -> Python list
    return []


def ask_question(number, total, item):
    """Ask one question. Returns (is_correct, points)."""
    choices = list(item["choices"])
    random.shuffle(choices)  # random: mix the A-D choices
    print(f"\nQuestion {number}/{total}: {item['question']}")
    for letter, choice in zip("ABCD", choices):
        print(f" {letter}. {choice}")

    start = time.perf_counter()  # time: start the stopwatch
    while True:
        reply = input("Your answer (A-D): ").strip().upper()
        if reply in ("A", "B", "C", "D"):
            break
        print("Please type a letter from the choices.")
    seconds = time.perf_counter() - start  # time: stop the stopwatch

    if choices["ABCD".index(reply)] != item["answer"]:
        print(f"Wrong! The correct answer is: {item['answer']} ({seconds:.1f}s)")
        return False, 0
    fast = seconds <= FAST
    points = POINTS + BONUS if fast else POINTS
    print(
        f"Correct! {'Fast answer bonus! ' if fast else ''}+{points} points ({seconds:.1f}s)"
    )
    return True, points


def play():
    with open(QUESTIONS_FILE) as f:
        questions = json.load(f)  # json: file -> list of questions
    name = input("Enter your name: ").strip() or "Player"

    default = min(5, len(questions))
    raw = input(
        f"How many questions? (1-{len(questions)}, Enter for {default}): "
    ).strip()
    if raw and not raw.isdigit():
        print(f"Not a number. Using {default}.")
    count = int(raw) if raw.isdigit() else default
    count = max(1, min(count, len(questions)))
    chosen = random.sample(questions, count)  # random: different questions each game

    print(f"\nGood luck, {name}! Answer within {FAST} seconds for a bonus.")
    time.sleep(1)  # time: short pause

    score = correct = 0
    game_start = time.perf_counter()
    for number, item in enumerate(chosen, start=1):
        is_correct, points = ask_question(number, count, item)
        correct += is_correct
        score += points
    total_seconds = time.perf_counter() - game_start

    print("\n" + "=" * 36)
    print(f"{'GAME OVER':^36}")
    print("=" * 36)
    print(f"Player : {name}")
    print(f"Correct : {correct}/{count} ({correct / count * 100:.0f}%)")
    print(f"Score : {score}")
    print(f"Time : {total_seconds:.1f} seconds")

    scores = load_scores()
    scores.append(
        {
            "name": name,
            "score": score,
            "correct": correct,
            "total": count,
            "seconds": round(total_seconds, 1),
            "date": time.strftime("%Y-%m-%d %H:%M"),
        }
    )  # time: date stamp
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)  # json: Python list -> file
    print("Score saved to high_scores.json")


def show_high_scores():
    scores = load_scores()
    if not scores:
        print("\nNo scores yet. Play a game first!")
        return
    best = sorted(scores, key=lambda s: (-s["score"], s["seconds"]))[:5]
    print("\n" + "=" * 52)
    print(f"{'TOP 5 HIGH SCORES':^52}")
    print("=" * 52)
    print(f"{'#':<3}{'Name':<12}{'Score':>6}{'Correct':>9}{'Time':>8} Date")
    for rank, s in enumerate(best, start=1):
        print(
            f"{rank:<3}{s['name']:<12}{s['score']:>6}"
            f"{str(s['correct']) + '/' + str(s['total']):>9}"
            f"{str(s['seconds']) + 's':>8} {s['date']}"
        )


def main():
    if not QUESTIONS_FILE.exists():
        print("questions.json not found. Put it in the same folder as quiz_game.py.")
        return
    print("=" * 36)
    print(f"{'PYTHON QUIZ GAME':^36}")
    print("=" * 36)
    while True:
        print("\n1. Play\n2. High scores\n3. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            play()
        elif choice == "2":
            show_high_scores()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
