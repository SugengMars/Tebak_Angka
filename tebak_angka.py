import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int( input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('sorry, guess again, too Law.')
        elif guess > random_number:
            print('sorry, guess again, too High.')

    print(f'yeyy!! congrats.. You have passed the number {random_number} complete')

guess(10)