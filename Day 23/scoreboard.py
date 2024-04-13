from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-270, 260)
        self.write(f"Level: {self.score}",move=False, align='left', font=FONT)
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}",move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",move=False, align='center', font=FONT)