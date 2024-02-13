from player import Player
from board import Board

board = Board()
player1 = Player(1)
player2 = Player(2)

player1_choice = player1.sign_choice()
player2_choice = player2.sign_choice()
while player2_choice == player1_choice:
    print("Player 2, you must choose a different sign than Player 1.")
    player2_choice = player2.sign_choice()
    
def restart_game(game_on):
    if not game_on:
        play_again = input("You wanna play again? Press Y if yes and N if no: ").upper()
        if play_again == "N":
            return False
        elif play_again == "Y":
            board.board_reset()
            player1.sign_choice()
            player2.sign_choice()
            return True 
    
    
game_on = True
while game_on:
    
    ## Player 1 Turn
    player1_turn = player1.play()
    board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    
    while board.valid_move is False:
        player1_turn = player1.play()
        board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    
    board.print_board()
    
    if board.check_horizontal_winner() or board.check_vertical_winner() or board.check_diagonal_winner():
        print(f"{player1.player_number} is the winner!")
        game_on = False
        game_on = restart_game(game_on)
    elif board.check_draw():
        print("It's a Draw! Try again.")
        game_on = False
        game_on = restart_game(game_on)


        
    ## Player 2 Turn  
    player2_turn = player2.play()
    board.add_signs(player2.player_row_decision, player2.player_column_decision, player2.player_choice)
    
    while board.valid_move is False:
        player2_turn = player2.play()
        board.add_signs(player2.player_row_decision, player2.player_column_decision, player2.player_choice)

    board.print_board()
    
    if board.check_horizontal_winner() or board.check_vertical_winner() or board.check_diagonal_winner():
        print(f"{player2.player_number} is the winner!")
        game_on = False
        game_on = restart_game(game_on)
    elif board.check_draw():
        print("It's a Draw! Try again.")
        game_on = False
        game_on = restart_game(game_on)
      
    
print("Thanks for playing!")

