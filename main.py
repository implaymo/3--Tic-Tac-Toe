from player import Player
from board import Board

board = Board()
player1 = Player()


def print_board(board):
    for row in board:
        print(*row)
        
    
print_board(board.board)