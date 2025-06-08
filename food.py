from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, size, color, shape, visible):
        super().__init__(shape, visible)
        self.size = size
        self.food_color = color
        self.penup()
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.color(color)
        self.speed("fastest")
        self.refresh()


    def get_position(self):
        return self.pos()

    def refresh(self):
        self.hideturtle()
        self.setpos(randint(-280,280),randint(-280,280))
        self.showturtle()