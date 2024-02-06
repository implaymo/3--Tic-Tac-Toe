board = [
    ["_", "|", "_", "|", "_"],
    ["_", "|", "_", "|", "_"],
    [" ", "|", " ", "|"," "]
    ]

def print_board():
    for row in board:
        print(*row)

loop_counter = 1
user_choice = input("Choose X or O: ").upper()
user_colum_decision = input("In which colum you want to put? Choose 0/2/4: ")
user_row_decision = input("In which row you want to put? Choose 0/2/4: ")
while loop_counter < 2:
    loop_counter += 1
    print_board()
