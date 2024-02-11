class Board():
    def __init__(self) -> None:
        self.board = [
                ["_", "|", "_", "|", "_"],
                ["_", "|", "_", "|", "_"],
                [" ", "|", " ", "|"," "]
                ]

    
    def add_signs(self, row, column, user_choice):
        if self.board[int(row)][int(column)] == "X" or self.board[int(row)][int(column)]  == "O":
            print("Position already choosen. Try again.")

        else: 
            self.board[int(row)][int(column)]  = user_choice

    def print_board(self):
        for row in self.board:
            print(*row)