class Player():
    def __init__(self) -> None:
        self.column = [0,2,4]
        self.row = [0,1,2]
        self.player_row_decision = 0
        self.player_column_decision = 0
        self.player_choice = ""

    def sign_choice(self):
        self.player_choice = input("Choose X or O: ").upper()
        while self.player_choice != "X" and self.player_choice != "O":
            print("Wrong choice. You must choose 'X' or 'O'")
            self.player_choice = input("Choose X or O: ").upper()
        return self.player_choice
    
    def column_choice(self):
        self.player_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
        while self.player_column_decision not in self.column:
            print("Wrong choice. You must choose 0, 2 or 4: ") 
            self.player_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
        return self.player_column_decision
    
    def row_choice(self):
        self.player_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
        while self.player_row_decision not in self.row:
            print("Wrong choice. You must choose 0, 1 or 2: ") 
            self.player_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
        return self.player_row_decision
     
    def play(self):
        self.column_choice()
        self.row_choice()