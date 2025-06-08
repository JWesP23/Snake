import turtle
import time

class Snake:

    def __init__(self, color, speed, starting_position, size):
        self.length = 3
        self.color = color
        self.speed = speed
        self.starting_position = starting_position
        self.size = size

        snake_head = turtle.Turtle(shape="square")
        snake_head.setpos(self.starting_position)
        snake_head.color(color)
        snake_head.penup()
        snake_head.shapesize(self.size/20, self.size/20)

        self.snake = [snake_head]
        self.snake_head = snake_head
        self.append_body()
        self.append_body()

    def append_body(self):
        snake_body = turtle.Turtle(shape="square")
        snake_body.penup()
        snake_body.color(self.color)
        snake_body.shapesize(self.size/20, self.size/20)
        tail = self.snake[-1]

        if self.snake_head.heading() == 0:
            snake_body.setpos(tail.xcor() - self.size, tail.ycor())
        elif self.snake_head.heading() == 90:
            snake_body.setpos(tail.xcor(), tail.ycor() - self.size)
        elif self.snake_head.heading() == 180:
            snake_body.setpos(tail.xcor() + self.size, tail.ycor())
        elif self.snake_head.heading() == 270:
            snake_body.setpos(tail.xcor(), tail.ycor() + self.size)

        self.snake.append(snake_body)
        self.length += 1


    def reset(self, screen):
        for segment in self.snake:
            segment.hideturtle()
        self.snake.clear()

        snake_head = turtle.Turtle(shape="square")
        snake_head.setpos(self.starting_position)
        snake_head.color(self.color)
        snake_head.penup()
        snake_head.shapesize(self.size/20, self.size/20)

        self.snake = [snake_head]
        self.snake_head = snake_head
        self.append_body()
        self.append_body()

        self.blink_snake(screen)


    def change_color(self, color):
        for segment in self.snake:
            segment.color = color


    def blink_snake(self, screen):
        for _ in range(3):
            for segment in self.snake:
                segment.hideturtle()
            screen.update()
            time.sleep(.25)
            for segment in self.snake:
                segment.showturtle()
            screen.update()
            time.sleep(.25)

    def get_length(self):
        return self.length


    def get_heading(self):
        return self.snake_head.heading()


    def get_speed(self):
        return self.speed


    def set_speed(self, speed):
        self.speed = speed


    def move(self):
        for _ in range(0,self.speed):
            for segment_index in range(len(self.snake) - 1, 0, -1):
                current_segment = self.snake[segment_index]
                next_segment = self.snake[segment_index - 1]

                current_segment.setpos(next_segment.xcor(),next_segment.ycor())

            self.snake_head.forward(20)


    def turn_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def turn_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def turn_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def turn_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)