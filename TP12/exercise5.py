import random

def cows_bulls(seed_value):
    random.seed(seed_value)
    correct = str(random.randint(0, 9999)).zfill(4)

    def game(guess):
        guess = str(guess).zfill(4)
        cows = sum(c == g for c, g in zip(correct, guess))
        bulls = sum(c in guess for c in correct) - cows
        return (cows, bulls)

    return game
