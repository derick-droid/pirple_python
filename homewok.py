# Create a function that takes in two parameters: rows, and columns, both of which are integers. The
# function should then proceed to draw a playing board (as in the examples from the lectures) the
# same number of rows and columns as specified. After drawing the board, your function should return True.

def playing_board(row, column):
    if row > 5:
        return False
    elif column > 6:
        return False

    for item in range(row):
        if item % 2 == 0:
            for num in range(column):
                if num % 2 == 1:
                    print(" ", end=" ")
                else:
                    print(" | ", end=" ")
        else:
            print("-----")

    return True


playing_board(5, 6)