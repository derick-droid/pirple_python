# syntax
counter = 1
sum = 0
while counter <= 10:
    print(counter)
    sum = sum + counter
    counter += 1
    

# print(sum)

# while loop and list
letters = ["a", "b", "c", "d", "e"]
index = 0
while (index < len(letters)):
    print(f" the element at index {index} is {letters[index]}")
    index += 1

# more with while loops in calculation
distance = 5000
speed = 50
time = 0
while distance > 0:
    distance = distance - speed
    time = time + 1

print(distance)
print(time)
    # another process 
while distance != 0 :
    time = speed / distance

print(time)