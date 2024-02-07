Player1_choice = input("Choose X or O: ").upper()
while Player1_choice != "X" and Player1_choice != "O":
    print("Wrong choice. You must choose 'X' or 'O'")
    Player1_choice = input("Choose X or O: ").upper()
    
column = [0,2,4]
row = [0,1,2]
    
Player1_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
while Player1_column_decision not in column:
    print("Wrong choice. You must choose 0, 2 or 4: ") 
    Player1_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
    
Player1_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
while Player1_row_decision not in row:
    print("Wrong choice. You must choose 0, 1 or 2: ") 
    Player1_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))

