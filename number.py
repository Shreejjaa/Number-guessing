import random

print('Bot: I am thinking of a number!')
SecretNumber = random.randint(1, 10)
attempts = 0

while True:
    Guess = int(input('Guess a number: '))
    attempts += 1
    if Guess == SecretNumber:
        print(f'Congratulations! You have guessed the number in {attempts} attempts.')
        break
    elif Guess < SecretNumber:
        print('Bot: Try for a higher number!')
    else:
        print('Bot: Try for a lower number!')
