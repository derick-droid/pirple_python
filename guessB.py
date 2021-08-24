
"""
the computer automatically makes the guess of random numbers
"""
from random import randint
import time 
current_time = time.CLOCK_PROCESS_CPUTIME_ID
randval = randint(1, 10)
upper_value = 10
lower_value = 1
guess = 5.0
while True:
    if guess == randval:
        print("the computer has won")
        break
    elif guess < randval:
        lower_value = guess

    else:
        upper_value = guess
    guess = (upper_value + lower_value) / 2

print(guess)
final_time = time.CLOCK_PROCESS_CPUTIME_ID
print(final_time - current_time)
