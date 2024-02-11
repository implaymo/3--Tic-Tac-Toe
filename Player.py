class Player():
    def __init__(self, player_number) -> None:
        self.column = ["0","2","4"]
        self.row = ["0","1","2"]
        self.player_row_decision = "0"
        self.player_column_decision = "0"
        self.player_choice = ""
        self.player_number = f"Player {player_number}"

    
    def sign_choice(self):
        self.player_choice = input(f"{self.player_number} Choose X or O: ").upper()
        if self.player_choice != "X" and self.player_choice != "O":
            print("Wrong choice. You must choose 'X' or 'O'")
            self.sign_choice()
        return self.player_choice
            
    def column_choice(self):
        try: 
            self.player_column_decision = input(f"{self.player_number} In which column do you want to put? Choose 0/2/4: ")
        except ValueError:
            print("Wrong choice. You must choose 0, 2 or 4") 
            self.column_choice()
        else:
            if self.player_column_decision not in self.column or len(str(self.player_column_decision)) > 1:
                print("Wrong choice. You must choose 0, 2 or 4: ") 
                self.column_choice()
    
    def row_choice(self):
        try: 
            self.player_row_decision = input(f"{self.player_number} In which row do you want to put? Choose 0/1/2: ")
        except ValueError:
            print("Wrong choice. You must choose 0, 1 or 2") 
            self.row_choice()
        else:
            if self.player_row_decision not in self.row or len(str(self.player_row_decision)) > 1:
                print("Wrong choice. You must choose 0, 1 or 2") 
                self.row_choice()
                

     
    def play(self):
        self.column_choice()
        self.row_choice()