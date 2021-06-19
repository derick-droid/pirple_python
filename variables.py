# global variables
one = 1
two = 2
three = 3
seven, six, eight = 7, 6, 8 # another way of defining a variable in shorten way

print(one)
print(two)
print(three)
two = 4
print(two)
# local variable


def function_name():
    global one   # accessing local variable into a function
    new_variable = 5  # local variable
    print(new_variable)
    print(one)
    return


function_name()

print(seven, six, eight)

# using count to declare variable
count = 0
count = count + 1 # adding zero to one
print(count)
count += 2
print(count)
count *= 2 # using multiplication
print(count)
count /= 3 # using division
print(count)
