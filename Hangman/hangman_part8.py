import random

words_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words_list)

def hide_word(word_to_hide, list_of_letters):
    for letter in word_to_hide:
        if letter not in list_of_letters:
            word_to_hide = word_to_hide.replace(letter, "-")
    return word_to_hide

def game():
    num_of_tries = 8
    guessed_letters = []
    all_input_letters = []
    word_start = hide_word(word, guessed_letters)

    while num_of_tries > 0:
        print(word_start)
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print('You should print a single letter\n')
            continue

        elif 97 > ord(guess) or ord(guess) > 122:
            print('It is not an ASCII lowercase letter\n')
            continue

        elif guess in all_input_letters:
            print('You already typed this letter\n')
            continue

        all_input_letters.append(guess)

        if guess in word and guess not in guessed_letters:
            guessed_letters.append(guess)
            word_start = hide_word(word, guessed_letters)
            print()
            if "-" not in word_start:
                print(word_start)
                print("You guessed the word!\n"
                      "You survived!")
                break

        else:
            num_of_tries -= 1
            if num_of_tries == 0:
                print("No such letter in the word\n"
                      "You are hanged!")
            else:
                print("No such letter in the word\n")

def menu():
    print("H A N G M A N\n")
    user_input = input('Type "play" to play the game, "exit" to quit: ')
    if user_input == "play":
        game()
    elif user_input == "exit":
        return;
    else:
        menu()
