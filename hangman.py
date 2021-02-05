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
guessed_words = []

# no of tries
tries = 8

# indefinite loop related to number of tries, once tries equals zero the game ends
while tries > 0:
# user letter input
    new_character = input("Input a letter: > ")
# to make sure the user input is one character/string
    if len(new_character) == 1:
# to check if user input in previous input
        if new_character in guessed_letters:
            print("You already guessed the letter", new_character)
# to check if user input in computer random choice
        elif new_character not in guess_word:
            print("That letter doesn't appear in the word")
# reduces the number of tries after failed attempt
            tries -= 1
            guessed_letters.append(new_character)
# confirmation of correct entry
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
            if "_" not in empty_word:
                guessed = True
    elif len(new_character) == len(guess_word):
        if new_character in guessed_letters:
            print("You already guessed the letter", new_character)
        elif new_character != guess_word:
            print("That letter doesn't appear in the word")
            tries -= 1
            guessed_letters.append(new_character)
        else:
            guessed = True
            empty_word = guess_word
            print(empty_word)
    else:
        print("That letter doesn't appear in the word")
        print(empty_word)
print("Thanks for playing!")
print("We'll see how well you did in the next stage")