
# drawing field function
def pattern(field):
    for row in range(5):  # 0, 1, 2, 3 , 4
        if row % 2 == 0:
            practical_row = int(row / 2)
            for col in range(5):  # 0, , 2, , 4
                if col % 2 == 0:
                    practical_col = int(col / 2)
                    if col != 4:
                        print(current_field[practical_col][practical_row], end="")
                    else:
                        print(current_field[practical_col][practical_row])
                else:
                    print("|", end="")
        else:
            print("-----")

# players playing


player = 1
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
pattern(current_field)
while True:
    print("player's turn: ", player)
    moveRow = int(input("enter row: "))
    if moveRow > 2:
        print("invalid choice please try again")
        break
    MoveCol = int(input("enter column: "))
    if MoveCol > 3:
        print("invalid choice please try again")
        break
    if player == 1:
        if current_field[MoveCol][moveRow] == " ":
            current_field[MoveCol][moveRow] = "x"
            player = 2
        else:
            print("already occupied")

    else:
        if current_field[MoveCol][moveRow] == " ":
            current_field[MoveCol][moveRow] = "0"
            player = 1
        else:
            print("already occupied")
    pattern(current_field)
