# getting message from user
name = input("enter your name: ")
print(name)
age = int(input("enter your age: "))  # converting a string into integer
print(str(age) + "1")  # converting integer to string

# using loop , list and output

scores = []
for i in range(3):
    current_score = float(input("enter your current score " + str(i+1) + " : "))  #  if we want to display sequential order of numbering
    print("the score you entered was : \n" + str(current_score))
    scores.append(current_score)

print(scores)
