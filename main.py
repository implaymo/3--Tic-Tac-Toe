from player import Player
from board import Board

board = Board()
player1 = Player(1)
player2 = Player(2)

player1.sign_choice()
player2.sign_choice()
while True:
    player1.play()
    board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    board.print_board()
    player2.play()
    board.add_signs(player2.player_row_decision, player2.player_column_decision, player2.player_choice)
    board.print_board()
