from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_player = 0
        self.l_player = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-30, 250)
        self.write(f"Score: {self.l_player}  |  {self.r_player}",move=False, align='center', font=('Arial', 24, 'normal'))
    
    def right_update_score(self):
        self.clear()
        self.r_player += 1
        self.write(f"Score: {self.l_player}  |  {self.r_player}",move=False, align='center', font=('Arial', 24, 'normal'))
    
    def left_update_score(self):
        self.clear()
        self.l_player += 1
        self.write(f"Score: {self.l_player}  |  {self.r_player}",move=False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",move=False, align='center', font=('Arial', 24, 'normal'))