import random

number = random.randint(1, 99)

def game():
    print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!''')
    attempt = 0
    while True:
        guess = input("What's your guess between 1 and 99?\n>> ")
        if input == "exit":
            print("Goodbye!")
            break
        try:
            guess = int(guess)
        except:
            print("That's not a number.")
            continue
        if guess < 1 or guess > 99:
            print("Out of range.")
            continue
        if guess < number:
            print("Too low!")
            attempt += 1
            continue
        if guess > number:
            print("Too high!")
            attempt += 1
            continue
        if guess == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("You won in {} attempts!".format(attempt))
            continue
        if guess == number:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(attempt))
            break


if __name__ == '__main__':
    game()