class Board():
    def __init__(self) -> None:
        self.board = [
                ["_", "|", "_", "|", "_"],
                ["_", "|", "_", "|", "_"],
                [" ", "|", " ", "|"," "]
                ]
        
    def add_signs(self, row, column):
       self.board[row][column]
       
    def print_board(self, position):
        for row in self.board:
            print(*row)