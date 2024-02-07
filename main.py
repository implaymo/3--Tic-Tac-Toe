board = [
    ["_", "|", "_", "|", "_"],
    ["_", "|", "_", "|", "_"],
    [" ", "|", " ", "|"," "]
    ]

def print_board():
    for row in board:
        print(*row)
        


user_choice = input("Choose X or O: ").upper()
while user_choice != "X" and user_choice != "O":
    print("Wrong choice. You must choose 'X' or 'O'")
    user_choice = input("Choose X or O: ").upper()
    
column = [0,2,4]
row = [0,1,2]
    
user_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
while user_column_decision not in column:
    print("Wrong choice. You must choose 0, 2 or 4: ") 
    user_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
    
user_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
while user_row_decision not in row:
    print("Wrong choice. You must choose 0, 1 or 2: ") 
    user_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
        

board[user_row_decision][user_column_decision] = user_choice

print_board()