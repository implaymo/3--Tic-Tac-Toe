Player2_choice = input("Choose X or O: ").upper()
while Player2_choice != "X" and Player2_choice != "O":
    print("Wrong choice. You must choose 'X' or 'O'")
    Player2_choice = input("Choose X or O: ").upper()
    
column = [0,2,4]
row = [0,1,2]
    
Player2_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
while Player2_column_decision not in column:
    print("Wrong choice. You must choose 0, 2 or 4: ") 
    Player2_column_decision = int(input("In which column do you want to put? Choose 0/2/4: "))
    
Player2_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))
while Player2_row_decision not in row:
    print("Wrong choice. You must choose 0, 1 or 2: ") 
    Player2_row_decision = int(input("In which row do you want to put? Choose 0/1/2: "))