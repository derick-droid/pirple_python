# if statement syntax

click = True
like = 0

if click == True:
    like = 1
    click = False

print(like)
# using equality

temperature = 20
thermo = 17
if temperature == 20:
    thermo = thermo + 1

if temperature >= 20:
    thermo = thermo + 5

if temperature <= 20:
    thermo = thermo + 10

if temperature > 20:
    thermo = thermo + 15

if temperature < 20:
    thermo = thermo +20

print(thermo)

# using logical operators

time  = "day"
spleep = True
pajamas = "off"
Inbed = True
if time == "night" and spleep == True: # when both of the conditions are true
    pajamas = "on"

print(pajamas)

if time == "night" or spleep == True: # when one of the conditions is true
    pajamas = "on"

elif time == "morning" and Inbed == True:
    pajamas = "off"
else:
    pajamas = "off"
    

print(pajamas)