with open('words.txt') as file:
    words_noisy = file.readlines()
words = []

for word in words_noisy:
    clean = word.strip()
    words.append(clean)
import random
word = random.choice(words)
guess = ["_"] * len(word)

print(guess)

for chance in range(15):
    x = input(f'plesae enter your character {chance} np.:')

    for i,c in enumerate(word):
        if c==x:
            guess[i] = x
    print(guess)


print(word,'is original word')





