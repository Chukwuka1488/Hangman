import random
print("H A N G M A N")

print()
print()

# list of words
prog_lang = ['python', 'java', 'kotlin', 'javascript']

# computer chooses from word
guess_word = random.choice(prog_lang)

# computer choice is hidden
empty_word = "-" * (len(guess_word))
print(empty_word)

# empty list
guessed_letters = []

# no of tries
tries = 8

# indefinite loop related to number of tries, once tries equals zero the game ends
while tries > 0:
# user letter input
    new_character = input("Input a letter: > ")
# to make sure the user input is one character/string
    if len(new_character) == 1:
# to check if user input in previous input
        if new_character not in guess_word:
            tries -= 1
            if tries > 0:
                print("That letter doesn't appear in the word")
                print()
                print(empty_word)
            else:
                print("That letter doesn't appear in the word")
                print("You lost!")
# to check if user input in computer random choice
        elif new_character in guessed_letters:
            tries -= 1
            if tries > 0:
                print("No improvements")
                print()
                print(empty_word)
            else:
                print("No improvements")
                print("You lost!")

        else:
            print()
            # adds entry to already guessed list
            guessed_letters.append(new_character)
            # convert the hidden guessed word to a list
            word_as_list = list(empty_word)
            # list comprehension to check user character and add to index of hidden word
            indices = [i for (i, letter) in enumerate(guess_word) if letter == new_character]
            for index in indices:
                word_as_list[index] = new_character
            # add the correct letter to the empty spacek

            empty_word = "".join(word_as_list)
            print(empty_word)
    if guess_word == empty_word:
    # if guess_word == empty_word:
        print("You guessed the word!")
        print("You survived!")
        break