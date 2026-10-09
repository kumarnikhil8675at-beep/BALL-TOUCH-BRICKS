from brick import bricks
from ball import balling
from score import scoreing
import turtle
import random
import time

screen = turtle.Screen()
screen.listen()
screen.setup(width=600, height=700)
screen.title("BALL TOUCH BRICKS")
screen.tracer(0)

paddle = bricks(0, -300)
paddle.shapesize(1, 3)

brick_list = []
ball_list = []
move_speed = 0.03


def create_bricks():
    colors = ["lime", "green", "cyan", "blue"]

    for y_position in [300, 250, 200, 150]:
        for x_position in range(-4, 5):
            if random.choice([0, 1, 1, 1, 1]):
                brick = bricks(x_position * 60, y_position)
                brick.pensize(5)
                brick.color(random.choice(colors))
                brick.shapesize(1, 2)
                brick_list.append(brick)


create_bricks()

ball = balling()
ball_list.append(ball)

score_display = scoreing((-280, 320))
game_over_display = scoreing((-200, 0))
game_over_display.clear()

retry_display = scoreing((-120, -50))
retry_display.clear()

game_running = True


def retry_game():
    global game_running, move_speed

    move_speed = 0.03
    game_running = True

    score_display.reset()
    brick_list.clear()
    create_bricks()

    new_ball = balling()
    ball_list.append(new_ball)

    retry_display.clear()
    game_over_display.clear()

    game_logic()


screen.onkeypress(
    fun=lambda: paddle.move()
    if paddle.pos() < (250.00, -300.00) else None,
    key="Right"
)

screen.onkeypress(
    fun=lambda: paddle.left()
    if paddle.pos() > (-250.00, -300.00) else None,
    key="Left"
)

screen.onkeypress(
    fun=lambda: retry_game() if not ball_list else None,
    key="r"
)


def game_logic():
    global game_running, move_speed

    while game_running:
        for current_ball in ball_list:
            time.sleep(move_speed)
            screen.update()

            current_ball.move()

            if current_ball.xcor() > 250 or current_ball.xcor() < -250:
                current_ball.wallbounce()

            if current_ball.ycor() > 320:
                current_ball.wallupper()

            if current_ball.ycor() < -330:
                move_speed = 0.02
                current_ball.clear()
                current_ball.hideturtle()
                ball_list.remove(current_ball)

            if current_ball.ycor() < -330 and not ball_list:
                game_over_display.write(
                    "GAME OVER",
                    font=("Arial", 50, "bold")
                )

                retry_display.write(
                    f"Press (R) for Retry\n     Your Score {score_display.value}",
                    font=("Arial", 20, "bold")
                )

                for brick in brick_list:
                    brick.clear()
                    brick.hideturtle()

                game_running = False

            if (
                current_ball.distance(paddle) < 50
                and current_ball.ycor() == -280
            ):
                current_ball.bounce()

            for brick in brick_list:
                if (
                    current_ball.distance(brick) < 33
                    and current_ball.ycor() in [300, 250, 200, 150]
                ):
                    brick.clear()
                    brick.hideturtle()
                    score_display.update()
                    brick_list.remove(brick)

            if not brick_list:
                create_bricks()

                new_ball = balling()

                if len(ball_list) < 2:
                    ball_list.append(new_ball)

                move_speed = 0.01

            screen.update()


game_logic()

screen.mainloop()