class Pets:
    def __init__(self, name, age, hungry, colour, ):
        self.name = name
        self.age = age
        self.hungry = hungry
        self.colour = colour

    # dfn getter method
    def getname(self):
        return self.name

    def getAge(self):
        return self.age

    def getHungry(self):
        return self.hungry

    def getColour(self):
        return self.colour
    # dfn setter method

    def setName(self, Xname):
        self.name = Xname
        return Xname

    def setAge(self, age):
        self.age = age

    def setHungry(self, hungry):
        self.hungry = hungry
        return hungry

    def setcolour(self, colour):
        self.colour = colour


class Dog(Pets):

    def __init__(self, breed, barks, name, age, hungry, colour):
        Pets.__init__(self, name, age, hungry, colour)
        self.breed = breed
        self.barks = barks

    def barking(self):
        if self.hungry == True:
            return f" The dog breed {self.breed} is hungry"

        else:
            return f"the {self.breed}, {self.name} is okay "

    # method changing attributes to string
    def __str__(self):
        return f"{self.name} likes to {self.barks}"


class Cat(Pets):
    def __init__(self, meows, playful, name, age, hungry, colour):
        Pets.__init__(self, name, age, hungry, colour)
        self.meows = meows
        self.playful = playful

    def wants_to_play(self):
        if self.playful == True:
            return  f"{self.name} wants to  {self.meows}"
        else:
            return f"{self.name} does not want play"
        # method changing the attributes to string
    def __str__(self):
        return f"{self.name} likes to {self.meows}"
# wants to check if person has pets


class Person:

    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def has_pets(self):
        if self.pet == 0:
            return f"{self.name}he has no pet"
        else:
            return f"{self.name} has pet(s)"


killva = Dog("wood", "barks", "killva", 6,True, "gery" )

nyasuba = Cat("meows", True, "nyasuba", 3, True, "white")
checking_person = Person("Okinda", [nyasuba, killva])
dog1 = killva.barking()
cat1 = nyasuba.wants_to_play()
print(dog1)
print(cat1)
print(killva)
print(checking_person.has_pets())
"""
accessing elements in the pet

"""
#  add name attribute to the element
print(checking_person.pet[0].name)