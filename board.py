class Board():
    def __init__(self) -> None:
        self.board = [
                ["_", "|", "_", "|", "_"],
                ["_", "|", "_", "|", "_"],
                [" ", "|", " ", "|"," "]
                ]

        
    def add_signs(self, row, column, user_choice):
       self.board[row][column] = user_choice
       
    def print_board(self):
        for row in self.board:
            print(*row)