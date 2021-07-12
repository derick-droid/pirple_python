# black shoes shelves with sizes customers choose the size they wish to buy
# if chosen the stock decreases and no one is allowed to choose zero and negative numbers

black_shoes = {45: 2, 32: 4, 44: 4, 23: 5, 40: 2}
while True:
    choice = int(input("enter your size: "))
    if choice <= 0:
        print("invalid shoe size")
    elif choice not in black_shoes:
        print("your size is not currently available")
    elif black_shoes[choice] <= 0:
        print("it is out of stock")
    else:
        black_shoes[choice] -= 1
        print("""
thank you for shopping with us 
your request is being processed
        """)
        print(black_shoes)