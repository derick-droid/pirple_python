# initialize the class

class compsci:
    def __init__(self,  classname = " name", classyear = 1):
        self.classname = classname
        self.classyear = 6


comp = compsci("computer science", 3)
comp1 = compsci("newyork", 5)

print(f"{comp.classname}")
print(f"{comp.classyear}")
print(f"{comp1.classname}")
print(f"{comp1.classyear}")
