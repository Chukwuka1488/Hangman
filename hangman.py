import random

print("H A N G M A N")
print()

# list of words
prog_lang = ['kotlin', 'python','java', 'javascript']

# computer chooses from word
guess_word = random.choice(prog_lang)

# computer choice is hidden
empty_word = "-" * (len(guess_word))
print(empty_word)

# empty list
guessed_letters = []
wrong_letters = []

# no of tries
tries = 8

# indefinite loop related to number of tries, once tries equals zero the game ends
while tries > 0:
    # user letter input
    new_character = input("Input a letter: ")
    # to make sure the user input is one character/string
    if len(new_character) != 1:
        print("You should input a single letter")
        print()
        print(empty_word)
    else:
        # continue
        if new_character.isalpha() is False:
            print("Please enter a lowercase English letter")
            print()
            print(empty_word)
            continue
        else:
            # continue
            if new_character != new_character.lower():
                print("Please enter a lowercase English letter")
                print()
                print(empty_word)
                continue
            else:
                # continue

                # to check if user input in previous input
                if new_character not in guess_word:

                    if tries > 0:
                        if new_character in wrong_letters:
                            print("You've already guessed this letter")
                            print()
                            print(empty_word)
                        else:
                            tries -= 1
                            if tries == 0:
                                print("That letter doesn't appear in the word")
                                print("You lost!")
                                break
                            else:
                                print("That letter doesn't appear in the word")
                                print()
                                print(empty_word)
                                wrong_letters.append(new_character)
                    else:
                        print("That letter doesn't appear in the word")
                        print("You lost!")

                elif new_character in guessed_letters:

                    if tries > 0:
                        print("You've already guessed this letter")
                        print()
                        print(empty_word)
                    else:
                        print("You've already guessed this letter")
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
                    # add the correct letter to the empty space

                    empty_word = "".join(word_as_list)
                    print(empty_word)
        if guess_word == empty_word:
            # if guess_word == empty_word:
            print(f"You guessed the word {empty_word}!")
            print("You survived!")
            break