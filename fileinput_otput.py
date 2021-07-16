# when we want to interact with files in our computer not the user directly
# general format
# file = open("filename", "r")
# file.close()  # it is good to close the files after completion to avoid errors in the file

cities = ["HongKong", "Nairobi", "kampala", "Lagos", ]
africa_cities = open("vacationCities", "w") # writing into a file
for city in cities:
    africa_cities.write(city + "\n")

africa_cities.close()
africa_cities = open("vacationCities", "r") # reading into a file
# reading elements line by line
first_line = africa_cities.readline()
print(first_line)
second_line = africa_cities.readline()
print(second_line)
third_line = africa_cities.readline()
print(third_line)
fourth_line = africa_cities.readline()
print(fourth_line)
# reading all elements in the file at once

The_whole_file = africa_cities.read()
print(The_whole_file)
africa_cities.close()  # closing the file

# appending into the file

another_city = "bujumbura"
africa_cities = open("vacationCities", "a")
africa_cities.write(another_city)
africa_cities.close()
africa_cities = open("vacationCities", "r")

for city in africa_cities:
    print(city + " \n")

africa_cities.close()
# to open a file without closing it at the end

with open("vacationCities", "r") as africa_cities:
    for city in africa_cities:
        print(city)