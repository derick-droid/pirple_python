
# syntax of a function 

def addnNumber (number):
    result =  number +  1
    return result


var = 3
print(var)
# using variable
var2 = addnNumber(var)
var3 = addnNumber(var2)
print(var2)
print(var3)
# using numbers
var4 = addnNumber(103)
print(var4)
# using float point numbers
var5 = addnNumber(2.15)
# using addition
var6 = addnNumber(2.1 + 5.6)
print(var5)
print(var6)
# using division
var7 = addnNumber(4.6/23)
# using multiplication
var8 = addnNumber(3 * 23)
print(var7)
print(var8)

# using two or more parameters
def addmore(number1, number2):
    result1 = number1 + 2
    result1 += number2 + 2
    return result1


sum = addmore(3, 5)
print(sum)

