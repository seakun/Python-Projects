import random


def hide_word(letters, lst = []):
    for letter in letters:
        if letter not in lst:
            letters = letters.replace(letter, "-")
    return letters


def hangman():
    print("H A N G M A N")
    print()
    words_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words_list)
    num_of_tries = 8

    word_start = hide_word(word)
    guessed_letters = []

    for i in range(num_of_tries):
        print(word_start)
        guess = input("Input a letter: ")
        if guess in word and guess not in guessed_letters:
            guessed_letters.append(guess)
            word_start = hide_word(word, guessed_letters)
            print()
        else:
            print("No such letter in the word\n")
    print("Thanks for playing!\nWe'll see how well you did in the next stage")


hangman()
