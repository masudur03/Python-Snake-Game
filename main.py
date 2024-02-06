import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



x= 3

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")




game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increse_score()
        snake.bigger_snake()




    if snake.head.xcor()> 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        score.reset()
        score.update_scoreboard()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:

            score.reset()
            score.update_scoreboard()
            snake.reset()



    snake.move()









screen.exitonclick()