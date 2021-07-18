# a program where participants enter data and is being evaluated

participant_number = 5
participant_data = []
registration_times = 0
participant_file = open("participants.txt", "w")
while registration_times < participant_number:
    temp_data = []
    name = input("enter your name please: ")
    temp_data.append(name)
    country = input("enter your country of origin: ")
    temp_data.append(country)
    age = int(input("enter your age: "))
    temp_data.append(age)
    participant_data.append(temp_data)
    registration_times += 1

#  looping through the participant data to write it in another file

for participant in participant_data:
    for data in participant:
        participant_file.write(str(data))
        participant_file.write(" ")
    participant_file.write("\n")

participant_file.close()

current_file = open("participants.txt", "r")
current_list = []
for data in current_file:
    current_data = data.strip("\n").split()
    # print(current_data)
    current_list.append(current_data)
    # print(current_list)

# want to determine how many equal age mates exist

age = {}

for part_age in current_list:
    temp_part_age = int(part_age[-1])  # accessing the last value in the list
    if temp_part_age in age:
        age[temp_part_age] += 1
    else:
        age[temp_part_age] = 1
print(age)

# finding the maximum age and most represented age
oldest = 0
youngest = 1000
Most_occurrence = 0
occurrence = 0
for varAge in age:
    if varAge > oldest:
        oldest = varAge
    if varAge < youngest:
        youngest = varAge
    if age[varAge] >= occurrence:
        occurrence = age[varAge]
        Most_occurrence = varAge

print(oldest)
print(youngest)
print(f"most occurring age is  : {Most_occurrence}, with {occurrence}")
current_file.close()
