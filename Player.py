class Player():
    def __init__(self) -> None:
        self.column = [0,2,4]
        self.row = [0,1,2]
    
    
    def play(self):
        pass
    
    def sign_choice(self):
        player_choice = input("Choose X or O: ").upper()
        while player_choice != "X" and player_choice != "O":
            print("Wrong choice. You must choose 'X' or 'O'")
            player_choice = input("Choose X or O: ").upper()
    
    def column_choice(self):
        player_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
        while player_column_decision not in self.column:
            print("Wrong choice. You must choose 0, 2 or 4: ") 
            player_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
    
    def row_choice(self):
        player_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
        while player_row_decision not in self.row:
            print("Wrong choice. You must choose 0, 1 or 2: ") 
            player_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
    