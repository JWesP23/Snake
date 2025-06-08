import turtle
import snake
from time import sleep
import food
import scoreboard

screen = turtle.Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

my_snake = snake.Snake(color= "white", speed=2, starting_position=(0,0), size=20)
new_food = food.Food(color="blue", shape="circle", size=0.8, visible=False)
scoreboard = scoreboard.Scoreboard(0)

screen.listen()
game_on = True

score = 0

while game_on:

    screen.update()
    sleep(0.1)
    my_snake.move()

    screen.onkeypress(key="w", fun=my_snake.turn_up)
    screen.onkeypress(key="s", fun=my_snake.turn_down)
    screen.onkeypress(key="a", fun=my_snake.turn_left)
    screen.onkeypress(key="d", fun=my_snake.turn_right)
    screen.onkeypress(key="Up", fun=my_snake.turn_up)
    screen.onkeypress(key="Down", fun=my_snake.turn_down)
    screen.onkeypress(key="Left", fun=my_snake.turn_left)
    screen.onkeypress(key="Right", fun=my_snake.turn_right)

    #check for contact with food
    if my_snake.snake_head.distance(new_food) < 30:
        score += 1
        new_food.refresh()
        my_snake.append_body()
        scoreboard.update_score(score)
        print("nom nom nom")

    #check for collision with wall
    if my_snake.snake_head.xcor() > 640 or my_snake.snake_head.xcor() < -640:
        #game_on = False
        scoreboard.reset()
        my_snake.reset(screen)
    elif my_snake.snake_head.ycor() > 560 or my_snake.snake_head.ycor() < -560:
        #game_on = False
        scoreboard.reset()
        my_snake.reset(screen)

    #check for collision with tail
    for segment in my_snake.snake[1:]:
        if my_snake.snake_head.distance(segment) < 5:
            #game_on = False
            scoreboard.reset()
            my_snake.reset(screen)


screen.exitonclick()