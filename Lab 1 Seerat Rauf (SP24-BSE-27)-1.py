# CSE325 - Software Construction and Development
# Lab 01: Setting Up the AI-Augmented Development Environment
# Seerat Rauf - SP24-BSE-27

# Scenario: the same Celsius-to-Fahrenheit converter, built once by hand
# and once with an AI assistant, then compared.


# Activity 1: Build it by hand first
# My first draft used integer-style division and gave wrong answers, it was
# caught by testing a known value (100C should be 212F). Fixed version:
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


print(celsius_to_fahrenheit(100))  # 212.0


# Activity 2: Build it again with AI assistance
# Comment typed into the editor:
# Convert Celsius to Fahrenheit, validate numeric input, handle non-numeric
# input gracefully
# AI version used true division from the start, added a type hint and a
# docstring, and wrapped input() in try/except.
def celsius_to_fahrenheit_ai(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def read_celsius():
    try:
        return float(input("Celsius: "))
    except ValueError:
        print("Please enter a number.")
        return None


# Activity 3: Compare honestly
# The AI version didn't get lucky, it defaulted to float division and input
# checking. The hand-written bug was a common mistake, not carelessness.

# Activity 4: Commit both, clearly labelled
# $ git init cse325-lab01 && cd cse325-lab01
# $ git add hand_written.py && git commit -m "Hand-written converter (found and fixed integer-division bug)"
# $ git add ai_assisted.py && git commit -m "AI-assisted converter (float division and input validation from first draft)"

if __name__ == "__main__":
    value = read_celsius()
    if value is not None:
        print(f"{value}C = {celsius_to_fahrenheit_ai(value)}F")


# ---------------------------------------------------------
# Graded Lab Tasks
# ---------------------------------------------------------

# Task 1: Build it by hand, on the clock, in the open
# Written with inline completion disabled and the chat panel closed, inside
# a repo called cse325-lab01, with at least 3 commits:
#   1. file first runs
#   2. first defect found/fixed (integer division)
#   3. finished
# Evidence: run these on your own machine and paste the output in the report
#   git log --format='%h %ad %s' --date=iso
#   python -VV

# Task 2: Rebuild it with AI on a branch called ai-build
# $ git checkout -b ai-build
# Evidence needed (must come from YOUR run, quoted exactly as the tool
# produced it, not paraphrased):
#   Prompt used             : <paste here>
#   Suggestion I rejected   : <paste here>
#   What was wrong with it  : <one sentence>


# Task 3: Compare using my own numbers
# Fill this in from your own git log and run:
#
# | Branch     | Minutes (from commit timestamps) | Lines of code | Defects hit | Commit hash |
# |------------|----------------------------------|---------------|-------------|-------------|
# | main       |                                  |               |             |             |
# | ai-build   |                                  |               |             |             |
#
# Where the AI helped: it added input validation and used float division
# without being asked.
# Where it cost time: reading and checking its extra code (docstring, hints)
# that I had to verify anyway.
# Overall: it was faster for the boilerplate, but I still had to test it.


# Task 4: Defend one difference
# Biggest difference: the AI version validates input with try/except (see
# read_celsius in this file, the try block), the hand-written one does not.
# I think it is a real improvement, not just a different habit, because a
# non-numeric input would crash the hand-written program with a ValueError.
# It costs only a few lines. The catch is that it only handles ValueError,
# so something like an EOF error on input() would still crash it.


# ---------------------------------------------------------
# Lab Assignment (Take-Home)
# ---------------------------------------------------------
# Small utility built twice: tip splitter
def split_tip(bill, tip_percent, people):
    total = bill * (1 + tip_percent / 100)
    return total / people


# Give the AI version to a classmate for five minutes and note what they
# broke (e.g. people = 0 gives ZeroDivisionError, negative bill accepted).
def split_tip_safe(bill, tip_percent, people):
    if bill < 0 or tip_percent < 0:
        raise ValueError("bill and tip must not be negative")
    if people < 1:
        raise ValueError("people must be at least 1")
    return bill * (1 + tip_percent / 100) / people


# ---------------------------------------------------------
# Viva Questions (basic, based on this lab)
# ---------------------------------------------------------

# Q1: Why use relative rather than exact checks like 100C = 212F?
# A: A known value is a quick way to catch a wrong formula, it's how the
# integer-division bug was found.

# Q2: What did the AI version do that the hand-written one did not?
# A: Used float division, added a type hint/docstring, and handled
# non-numeric input.

# Q3: Why commit at least three times instead of once at the end?
# A: The commit history shows the work was done step by step, with
# timestamps, which is the evidence for the time comparison.

# Q4: Does the AI always give the right answer?
# A: No. Its output must be tested and understood by the developer, who
# stays responsible for deciding whether it is right.

# Q5: What is agent mode in Copilot Chat?
# A: A mode where the assistant can read the whole workspace, run commands
# and iterate on its own output, unlike plain inline completion.
