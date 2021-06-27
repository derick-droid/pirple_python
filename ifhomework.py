# Create a function that accepts 3 parameters and checks for equality between any two of them.

# Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.

def comparison (one, two, three):
     
    if one == two and three:
        return True
    else:
        return False


output =   comparison(int("5"), 3, 4 )
print(output)
        
