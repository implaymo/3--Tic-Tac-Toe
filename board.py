

class Board():
    def __init__(self) -> None:
        self.board = [
                ["_", "|", "_", "|", "_"],
                ["_", "|", "_", "|", "_"],
                [" ", "|", " ", "|"," "]
                ]
        self.valid_move = True
        self.winning_amount = 3


        
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
            
    def check_vertical_winner(self):
        for row in range(0,5,2):
            count_X = 0
            count_O = 0
            for column in self.board:
                if column[row] == "X":
                    count_X += 1
                elif column[row] == "O":
                    count_O += 1
            
            if count_X == self.winning_amount:
                return True  
            if count_O == self.winning_amount:
               return True

    def check_horizontal_winner(self):
       for row in self.board:
            count_X = 0
            count_O = 0
            for column in range(0,5,2):
                if row[column] == "X":
                    count_X += 1
                if row[column] == "O":
                    count_O += 1
                    
            if count_X == self.winning_amount:
               return True
            if count_O == self.winning_amount:
               return True
    
    def check_diagonal_winner(self):
        positions = []
        for i in self.board:
            for j in i[::2]:
                positions.append(j)
        
        if positions[0] == "X" and positions[4] == "X" and positions[8] == "X":
            return True
        elif positions[0] == "O" and positions[4] == "O" and positions[8] == "O":
            return True
        elif positions[2] == "X" and positions[4] == "X" and positions[6] == "X":
            return True
        elif positions[2] == "O" and positions[4] == "O" and positions[6] == "O":
            return True    
                
    def check_draw(self):
        for row in self.board:
            for element in row[::2]:
                if element != "X" and element != "O":
                    return False
        return True