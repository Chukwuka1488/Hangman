import random

print("H A N G M A N")

prog_lang = ['python', 'java', 'kotlin', 'javascript']

guess_word = random.choice(prog_lang)

first_3 = guess_word[:3]

last_n = guess_word[3:len(guess_word):1]

fill_word = "-" * (len(guess_word) - 3)

print(f"Guess the word {first_3}{fill_word}: >")

possible_word = input()

if guess_word == possible_word:
    print("You survived!")
else:
    print("You lost!")
