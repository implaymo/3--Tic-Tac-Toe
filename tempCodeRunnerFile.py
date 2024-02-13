    if play_again == "N":
            game_on = False
        elif play_again == "Y":
            game_on = True
            board.board_reset()
            player1.sign_choice()
            player2.sign_choice()