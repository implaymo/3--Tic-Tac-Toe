class Player():
    def __init__(self, player_number, board) -> None:
        self.column = ["0","2","4"]
        self.row = ["0","1","2"]
        self.player_row_decision = "0"
        self.player_column_decision = "0"
        self.player_choice = ""
        self.player_number = f"Player {player_number}"
        self.valid_move = True
        
        self.board = board
        

    
    def sign_choice(self):
        self.player_choice = input(f"{self.player_number} Choose X or O: ").upper()
        if self.player_choice != "X" and self.player_choice != "O":
            print("Wrong choice. You must choose 'X' or 'O'")
            self.sign_choice()
        return self.player_choice
            
    def choose_column(self):
        try: 
            self.player_column_decision = input(f"{self.player_number} In which column do you want to put? Choose 1/2/3: ")
            if self.player_column_decision == "1":
                self.player_column_decision = "0"
            elif self.player_column_decision == "3":
                self.player_column_decision = "4"
        except ValueError:
            print("Wrong choice. You must choose 1, 2 or 3") 
            self.choose_column()
        else:
            if self.player_column_decision not in self.column or len(str(self.player_column_decision)) > 1:
                print("Wrong choice. You must choose 1, 2 or 3: ") 
                self.choose_column()
    
    def choose_row(self):
        try: 
            self.player_row_decision = input(f"{self.player_number} In which row do you want to put? Choose 1/2/3: ")
            if self.player_row_decision == "1":
                self.player_row_decision = "0"
            elif self.player_row_decision == "2":
                self.player_row_decision = "1"
            elif self.player_row_decision == "3":
                self.player_row_decision = "2"

        except ValueError:
            print("Wrong choice. You must choose 1, 2 or 3") 
            self.choose_row()
        else:
            if self.player_row_decision not in self.row or len(str(self.player_row_decision)) > 1:
                print("Wrong choice. You must choose 1, 2 or 3") 
                self.choose_row()
                
    def player_turn(self):
        self.play()
        
        self.board.add_signs(self.player_row_decision, self.player_column_decision, self.player_choice)
        while self.board.valid_move is False:
            self.play()
            self.board.add_signs(self.player_row_decision, self.player_column_decision, self.player_choice)
     
    def play(self):
        self.choose_column()
        self.choose_row()
        
    
        

            