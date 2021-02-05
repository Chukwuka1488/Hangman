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