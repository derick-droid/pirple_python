from random import randint

guess_number = randint(0, 1000)

while True:
    guess = int(input("enter your gues (1-1000): "))
    if guess == guess_number:
        print("congratulation you won with guess", guess)
        break
    elif guess > guess_number:
        print("your guess is too high")
    else:
        print("your guess is too low")
