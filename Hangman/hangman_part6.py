import random

# Write your code here
print("H A N G M A N")
print("")

# computer takes random word
r = random.choice(['python', 'java', 'kotlin', 'javascript'])
new_word = []
# word split up into elements
split = list(r)
for i in range(len(split)):
    new_word.append("-")
print(str("".join(new_word)))

# asking user for letter
i = 8
while i != 0:
    print("Input a letter:", end='')
    new_letter = input().strip()
    # case if letter not in word
    if new_letter not in split:
        print("No such letter in the word")
        i -= 1
    # checking if the user has already asked for this letter
    if new_letter in new_word:
        print("No improvements")
        i -= 1
        # end game if user loses all tries
    if "-" in new_word and i == 0:
        print("You are hanged!")
        break
    print("")
    # checking if letter is in the word
    for p, e in enumerate(split):
        if e == new_letter:
            new_word[p] = new_letter
            # checking if the letter has already been asked
    print(str("".join(new_word)))
    # end game if user got the word
    if new_word == split:
        print("You guessed the word!")
        print("You survived!")
        break

