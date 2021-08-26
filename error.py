"""
error handling in python
"""
value = "123455"
try:
    print(int(value))
except:
    pass  # pass keyword is to allow the program to ignore
    print("exception handled")

print("it is done")

"""
when we want the real error
"""
value1 = "hey derrick"
try:
    raise NameError
    # print(int(input(value1)))

except Exception as real:
    print(str(real))
except ZeroDivisionError:  # being specific with the error
    print("we have an error ")
    raise
finally:
    print("it is over")

print("past the exception")