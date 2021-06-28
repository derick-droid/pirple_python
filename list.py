# list syntax
scores = [70, 55, 60.77, 86, 90]
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])

# accssing from the last element
print()

print(scores[-1])
print(scores[-2])
print(scores[-3])
print(scores[-4])
print(scores[-5])

# printing a range value of elements
print(scores[0:2]) # printing elements from index zero to index two but ignoring the element at index two
print(scores[1:]) # printing form index one to the last element

# changing values inside a list
scores[0] = 95
print(scores)
scores[2:3]  = []
scores[1:3]  = []
print(scores)
scores[1] = ["hello", "world"] # list inside a list
print(scores)
print(scores[1]) # accessing the list in list the larger list
 # accessing an element in the nested list
print(scores[1][0])
# adding element into the list 
scores.append(34)
print(scores)