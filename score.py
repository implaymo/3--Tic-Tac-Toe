class Score():
    def __init__(self) -> None:
        self.player1_score = 0
        self.player2_score = 0
    
    def update_score(self, player1_number, player2_number):
        print(f"SCORE: {player1_number}= {self.player1_score} vs {player2_number}= {self.player2_score}")
    