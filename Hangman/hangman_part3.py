# Write your code here
import random

print("H A N G M A N")
print("Guess the word: ")
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
guess = input()
if guess == word:
    print("You survived!")
else:
    print("You are hanged!")
