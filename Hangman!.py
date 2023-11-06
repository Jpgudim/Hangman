"""
This is a program meant to replicate the game of hangman

"""
import random


# A list of words to be used in the game
words = ["describe", "testing", "python", "computer", "apple", "keyboard", "university"]

word_to_guess = random.choice(words)

print("\nWelcome to hangman!")
print("Guess letters, and if you are wrong, the man gets closer to the sharks! ") 
print("Keep guessing letters, and if you can guess the word, before the man sinks, you win!\n")

print("    -----     ")
print("    |   |     ")
print("        |     ")
print("        |     ")
print("        |     ")
print("        |     ")
print("     ___|___  \n")

for item in word_to_guess:
    print ("_", end =" ")
print("\n")


"""
print("    -----     ")
print("    |   |     ")
print("    o   |     ")
print("   /|\  |     ")
print("   / \  |     ")
print("        |     ")
print("     ___|___  \n")
"""

letter = input("Guess a letter!: ")
if letter in word_to_guess:
    # loop through word to guess and find indexes
    print()
else:
    print("That letter is not in the word! A body part has been added")
print("    -----     ")
print("    |   |     ")
print("    o   |     ")
print("        |     ")
print("        |     ")
print("        |     ")
print("     ___|___  \n")


