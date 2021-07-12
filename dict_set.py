# sets
# syntax
# sets do not maintain the order of elements
# sets = {"element1", "element2", "element3", "element1"}
# sets do not repeat any elements
# print(sets)
# if "element1" in sets:
#     print("yes")
# else:
#     print("No")

# converting a list to a set

# country_list = []
# for person in range(10):
#     country = input("enter your country: ")
#     country_list.append(country)
#
# country_set = set(country_list)
# print(country_list)
# print(country_set)
# print()

# DICTIONARIES
# syntax
# adding value from the list into into the dictionary
nations_list = []
nation_dictionary = {"l" : 8}
for individual in range(5):
    nation = input("enter nation: ")
    nations_list.append(nation)

print(nations_list)
for item in nations_list:
    if item in nation_dictionary:
        nation_dictionary[item] += 1

    else:
        nation_dictionary[item] = 1
print(nation_dictionary)
