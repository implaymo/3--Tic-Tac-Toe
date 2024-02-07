board = [
    ["_", "|", "_", "|", "_"],
    ["_", "|", "_", "|", "_"],
    [" ", "|", " ", "|"," "]
    ]

def print_board():
    for row in board:
        print(*row)
        
        
### Way of getting Players answer on the board
# board[first_user_row_decision][first_user_column_decision] = first_user_choice



print_board()