# Write your code here
import random

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
guess = input()

word_formatted = guess[0:3]

for i in range(0, len(guess) - 3):
    word_formatted += "-"

print(f"Guess the word: {word_formatted}")
if guess == word:
    print("You survived!")
else:
    print("You are hanged!")
