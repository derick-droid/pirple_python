# how to use breaks and continue  in loops 
participants = ["jane", "collo", "derrick", "charles", "swalleh"]

for name in participants:
    if name == "derrick":
        print(participants.index(name))


# continue function
for number in range(10):
    if number % 3 == 0:
        print(number)
        print("divisible by 3")
    print(number)
    print("Not divisible by 3")
