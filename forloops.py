
# syntax for for loop
words = "hello world"
letters = []
for letter in words:
    print(letter)
    if letter == "o":
        print("what a wonderfull letter")

    letters.append(letter)
print(letters)
# looping through the list created
for element in letters:
    print(element)
print()
# definig a list containing number
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    # print(number)
    if number % 2 == 0:
        print(f"{number} is even ")
    else:
        print(f"{number} is odd")

print()
# using range function in for loop

values = []
for num in range (100):
    values.append(num)
    print(num)
print(values)

# giving patterns in range values
for m in range (1, 10, 2):
    print(m)
    values.append(m)

print(values)
# using negative number
for n in range (-1, -12, -2):
    print(n)

