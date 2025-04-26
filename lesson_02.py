import os
import io
import sys
import time
import importlib
import student_code

# Helper functions
def pause(x=2):
    time.sleep(x)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def capture_output(func):
    """Captures the output of a function that prints to the console."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func()
    finally:
        sys.stdout = sys.__stdout__
    return captured_output.getvalue().splitlines()

def loading_dots(text="Reloading", dots=3, delay=0.5):
    print(color_text(text, "1;36"), end='', flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(color_text(".", "1;36"), end='', flush=True)
    print("\n")

import random

def fireworks(end=False):
    fireworks_frames = [
        "            .",
        "            .        *",
        "      *         .        .",
        "            .    *     .",
        "      .   *       *    .",
        "            .     *    .",
        "    *      .   *     .     *",
        "            .  *   *    .",
        "      .       *      .     *",
        "            🎆🎆🎆🎆🎆",
        "          🎇🎇🎇🎇🎇🎇",
        "        🎆🎇🎆🎇🎆🎇🎆",
        "     G  🎆🎇🎆🎇🎆🎇",
        "     GR   🎆🎇🎆🎇🎆",
        "     GRE    🎆🎇🎆🎇",
        "     GREA     🎆🎇🎆",
        "     GREAT      🎆🎇",
        "     GREAT",
        "     GREAT J      🎆🎇",
        "     GREAT JO     🎆🎇🎆",
        "     GREAT JOB    🎆🎇🎆🎇",
        "     GREAT JOB!   🎆🎇🎆🎇🎆",
        "     GREAT JOB!  ",
        " 🎆 GREAT JOB!         🎆🎆🎆🎆🎆🎆",
        "        GREAT JOB!    🎇🎇🎇🎇🎇🎇🎇🎇🎇",
        "GREAT JOB! ",
    ]

    for frame in fireworks_frames:
        clear_console()
        print(color_text(frame, "1;35"))  # Solid magenta for initial fireworks
        pause(0.2)

    if end:
        end_game_frames = [
            "🎆 GREAT JOB! 🎆",
            "🎇 GREAT JOB! 🎇",
            "🎆 GREAT JOB! 🎆",
            "🎇 GREAT JOB! 🎇",
            "🎆 REAT JOB!  🎆",
            "🎇 EAT JOB!   🎇",
            "🎆 AT JOB!    🎆",
            "🎇 T JOB!     🎇",
            "🎆 JOB!      🎆",
            "🎇 OB!       🎇",
            "🎆 B!        🎆",
            "🎇 !         🎇",
            "🎆           🎆",
            "🎇           🎇",
            "🎆          G🎆",
            "🎇         GA🎇",
            "🎆        GAM🎆",
            "🎇       GAME🎇",
            "🎆      GAME 🎆",
            "🎇     GAME O🎇",
            "🎆    GAME OV🎆",
            "🎇   GAME OVE🎇",
            "🎆  GAME OVER🎆",
            "🎇 GAME OVER!🎇",
            "🎆GAME OVER! 🎆",
            "🎇AME OVER!  🎇",
            "🎆ME OVER!   🎆",
            "🎇E OVER!    🎇",
            "🎆 OVER!     🎆",
            "🎇VER!       🎇",  
            "🎆ER!        🎆",
            "🎇R!         🎇",
            "🎆!          🎆",
            "🎇           🎇",
        ]

        # Flash random colors across GAME OVER frames
        colors = ["1;31", "1;33", "1;32", "1;36", "1;35", "1;34"]  # Red, Yellow, Green, Cyan, Magenta, Blue

        for frame in end_game_frames * 2:  # Loop twice for full flash
            clear_console()
            random_color = random.choice(colors)
            print(color_text(frame, random_color))
            pause(0.15)

        pause(2)
        clear_console()
        print(color_text("\n👋 Goodbye!", "1;31"))
        exit()


# Missions
missions = [
    {
        "lesson": """📚 LESSON: What is an Iterable?
An iterable is something you can loop over in Python.
Lists, strings, dictionaries, and sets are all examples of iterables.
If you can "go through" it one item at a time, it's an iterable!

Example:
    favorite_animals = ['dog', 'cat', 'elephant']

We can loop over this list to print each animal!""",
        "text": "Create a list called favorite_animals with at least 3 animals.",
        "check": lambda sc: (
            hasattr(sc, 'favorite_animals')
            and isinstance(sc.favorite_animals, list)
            and len(sc.favorite_animals) >= 3
        ),
        "hint": "Hint: Example - favorite_animals = ['dog', 'cat', 'rabbit']"
    },
    {
        "lesson": """📚 LESSON: What is a Loop?
A loop lets you repeat actions many times.
In Python, a 'for' loop lets you go through each item in an iterable.

Example:
    for animal in favorite_animals:
        print(animal)

Each time, the variable 'animal' becomes the next item in the list!""",
        "text": "Use a for loop in the print_animals() function to print each animal.",
        "check": lambda sc: (
            hasattr(sc, 'print_animals')
            and callable(sc.print_animals)
            and hasattr(sc, 'favorite_animals')
            and isinstance(sc.favorite_animals, list)
            and len(sc.favorite_animals) >= 3
            and len(capture_output(sc.print_animals)) >= 3
            and all(
                animal.lower() in ' '.join(capture_output(sc.print_animals)).lower()
                for animal in sc.favorite_animals
            )
        ),
        "hint": "Hint: Use 'for animal in favorite_animals:' inside your function."
    },
    {
        "lesson": """📚 LESSON: What is a Conditional?
A conditional lets your code make decisions.
In Python, we use 'if' statements to check if something is true and do something special.

Example:
    if animal == 'dog':
        print('This is my favorite!')

Conditionals help your programs react differently based on what's happening!""",
        "text": "Modify print_animals() to print 'This is my favorite!' next to your favorite animal.",
        "check": lambda sc: (
            hasattr(sc, 'print_animals')
            and any(
                animal.lower() in line.lower() and "favorite" in line.lower()
                for line in capture_output(sc.print_animals)
                for animal in getattr(sc, 'favorite_animals', [])
            )
        ),
        "hint": "Hint: Inside your loop, add an if-statement checking if the animal is your favorite."
    }
]

# Lesson runner
mission_index = 0

# 🌟 Special Intro
clear_console()
print(color_text("\n👋 Welcome to your Python Adventure!", "1;36"))
print(color_text("\nToday you'll learn about Iterables, Loops, and Conditionals.", "1;35"))
print(color_text("\nYou'll make changes to your student_code.py file as you go.", "1;32"))
print(color_text("\nSave your file, then press 'r' to reload and test your code!", "1;33"))
input(color_text("\nPress ENTER to begin your first mission!", "1;36"))

# 🌟 Main mission loop
while mission_index < len(missions):
    current_mission = missions[mission_index]

    clear_console()
    print(color_text(f"\n🌟 Mission {mission_index + 1} of {len(missions)}", "1;36"))
    print("\n" + color_text(current_mission["lesson"], "1;35"))
    pause(6)

    print("\n" + color_text("🚀 " + current_mission["text"], "1;36"))

    while True:
        choice = input("\nType 'r' to reload your code, or 'q' to quit: ").lower()

        if choice == 'q':
            print(color_text("\n👋 Goodbye!", "1;31"))
            exit()

        if choice == 'r':
            try:
                loading_dots("🔄 Reloading")
                importlib.reload(student_code)
                print(color_text("✅ Code reloaded!", "1;32"))

                if current_mission["check"](student_code):
                    print(color_text("\n🎯 Mission accomplished!", "1;32"))
                    pause(2)
                    mission_index += 1
                    if mission_index == len(missions):
                        print(color_text("\n🎉 All missions completed! Fantastic job!", "1;32"))
                        fireworks(end=True)
                        break
                    fireworks()
                    break
                    
                else:
                    print(color_text("\n🛡️ Not quite yet. Save and reload when ready!", "1;33"))
                    print(color_text(current_mission["hint"], "1;33"))

            except Exception as e:
                print(color_text("\n❌ Error reloading student code:", "1;31"))
                print(color_text(str(e), "1;31"))

pause(2)
print(color_text("\n🎉 All missions completed! Fantastic job!", "1;32"))
pause(2)
