"""
Um pequeno programa: adivinhe o número

Ao executar esse programa, a saída terá
uma aparência semelhante a:
I am thinking of a number between 1 and 20.
Take a guess:
10
Your guess is too low.
Take a guess:
15
Your guess is too low.
Take a guess:
17
Your guess is too high.
Take a guess:
16
Good job! You guessed my number in 4 guesses!
"""

import random
secretNumber = random.randint(1, 20)
print('I am thinking od a number between 1 and 20.')

# Peça para o jogador adivinhar 6 vezes.
for guessesTaken in range(1, 7):
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('You guess is too low.')
    elif guess > secretNumber:
        print('You gues is too hight.')
    else:
        break  # Esta condição corresponde ao palpite correto!

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}')
