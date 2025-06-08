from turtle import Turtle

class Scoreboard:

    def __init__(self, starting_score):
        with open("high_score.txt", mode= "r") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.score = starting_score
        self.scoreboard.setpos(0,500)
        self.update_score(0)

    def update_score(self, new_score):
        self.scoreboard.clear()
        self.score = new_score
        self.scoreboard.write(f"Score: {new_score} High Score: {self.high_score}", align= "center", font= ("Courier", 24, "normal"))

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode= "w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.update_score(0)

    def game_over(self):
        self.scoreboard.clear()
        self.scoreboard.setpos(0,50)
        self.scoreboard.write(f"GAME OVER\nFinal Score:{self.score}", align= "center", font= ("Courier", 24, "normal"))