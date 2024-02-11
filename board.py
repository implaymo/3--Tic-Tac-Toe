

class Board():
    def __init__(self) -> None:
        self.board = [
                ["_", "|", "_", "|", "_"],
                ["_", "|", "_", "|", "_"],
                [" ", "|", " ", "|"," "]
                ]
        self.valid_move = True
        
    def add_signs(self, row, column, user_choice):
        if self.board[int(row)][int(column)] == "X" or self.board[int(row)][int(column)]  == "O":
            print("Position already choosen. Try again.")
            self.valid_move = False
        else: 
            self.valid_move = True
            self.board[int(row)][int(column)]  = user_choice

    def print_board(self):
        for row in self.board:
            print(*row)
            
    def check_if_winner(self):
        for row, inner_list in enumerate(self.board): 
            for column, element in enumerate(inner_list): 
                pass
            
    