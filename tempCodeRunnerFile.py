game_on = True
while game_on:
    if board.check_horizontal_winner() or board.check_vertical_winner():
        game_on = False
        break
    
    player1_turn = player1.play()
    board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    
    while board.valid_move is False:
        player1_turn = player1.play()
        board.add_signs(player1.player_row_decision, player1.player_column_decision, player1.player_choice)
    
    board.print_board()
        
    player2_turn = player2.play()
    board.add_signs(player2.player_row_decision, player2.player_column_decision, player2.player_choice)
    
    while board.valid_move is False:
        player2_turn = player2.play()
        board.add_signs(player2.player_row_decision, player2.player_column_decision, player2.player_choice)

    board.print_board()