from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode = "r") as file:
            saved_high_score = file.read()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.high_score = int(saved_high_score)
        self.color("white")
        self.goto(x= 0, y= 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score} ", move=False, align="center", font=("Arial", 16, "normal"))




    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode = "w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0

    def increse_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg= "GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))


