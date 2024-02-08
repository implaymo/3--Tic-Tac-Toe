from player import Player
from board import Board

board = Board()
player1 = Player()

player1.sign_choice()
while True:
    player1.play()
    board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    board.print_board()
