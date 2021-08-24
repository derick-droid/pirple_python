"""
other alternative means of importing
from random import * -- this is to import everything
"""
from random import uniform, randint, random, choice, shuffle
randInt = randint(1, 10)
print(randInt)

rand_uniform = uniform(1, 10)
print(rand_uniform)
randRandom = random()
print(randRandom)

"""
random numbers in a list
"""
number_list = [1, 2, 3, 5, 6, 7, 12, 11]
choice_number = choice(number_list)
print(choice_number)

# shuffling the elements in the list

number_shuffle = shuffle(number_list)
print(number_list)
