from player import Player
from board import Board

board = Board()
player1 = Player(1, board=board)
player2 = Player(2, board=board)

player1_choice = player1.sign_choice()
player2_choice = player2.sign_choice()
while player2_choice == player1_choice:
    print("Player 2, you must choose a different sign than Player 1.")
    player2_choice = player2.sign_choice()
    
def restart_game(game_on):
    if not game_on:
        play_again = input("You wanna play again? Press Y if yes and N if no: ").upper()
        if play_again == "N":
            print("Thanks for playing!")
            exit()
        elif play_again == "Y":
            board.board_reset()
            player1.sign_choice()
            player2.sign_choice()
            return True 
        
def game_over(game_on, player):
        if board.check_horizontal_winner() or board.check_vertical_winner() or board.check_diagonal_winner():
            print(f"{player} is the winner!")
            game_on = False
            game_on = restart_game(game_on)
        elif board.check_draw():
            print("It's a Draw! Try again.")
            game_on = False
            game_on = restart_game(game_on)
        return game_on
    
board.print_board()
game_on = True
while game_on:
    
    player1.player_turn()

    game_over(game_on, player="Player 1")
        
    player2.player_turn()
    
    game_over(game_on, player="Player 2")
      
    

