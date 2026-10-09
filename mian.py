from brick import bricks
from ball import balling
from score import scoring
import turtle
import random
import time

screen=turtle.Screen()
screen.listen()
screen.setup(width=600,height=700)
screen.title("BALL TOUCH BRICKS")
screen.tracer(0)

bat=bricks(0,-300)
bat.shapesize(1,3)


brick_list=[]
def wall_maker():
    COLORS = ["lime", "green", "cyan", "blue"]
    for a in [300,250,200,150]:
        for b in range(-4,5):
            if random.choice([0, 1, 1, 1, 1]):
                blod=bricks(b*60,a)
                blod.pensize(5)
                blod.color(random.choice(COLORS))
                blod.shapesize(1,2)
                brick_list.append(blod)
            
wall_maker()
ball=balling()
scores=scoring((-280,320))
game_over=scoring((-200,0))
game_over.clear()
retry=scoring((-120,-50))
retry.clear()

loop_run=True
def Retry():
    scores.reset()
    
    brick_list.clear()
    ball.resetposion()
    
    retry.clear()
    game_over.clear()
    
    global loop_run
    loop_run=True
    Game_logic()
    


screen.onkeypress(fun=lambda :bat.move() if bat.pos() < (250.00,-300.00) else None,key="Right")
screen.onkeypress(fun=lambda :bat.left() if bat.pos() > (-250.00,-300.00) else None,key="Left")
screen.onkeypress(fun=lambda :Retry() if ball.ycor() < -330 else None ,key="r")

def Game_logic():
    global loop_run      
    while loop_run:
        time.sleep(ball.movespeed)
        screen.update()
        ball.move()
        
        if ball.xcor()>250  or ball.xcor()<-250:
            ball.wallbounce()
        
        if ball.ycor()>320:
            ball.wallupper()
        
        if ball.ycor()<-330:
            game_over.write("GAME OVER",font=("Arial",50,"bold"))
            retry.write(f"Press (R) for Retry \n    Your Score {scores.value}",
                        font=("Arial",20,"bold"))
            for a in brick_list:
                a.clear()
                a.hideturtle()
            loop_run=False
            
    
        if ball.distance(bat) <50 and ball.ycor() == -280:
            ball.bounce()
        
        for a in brick_list:
            if ball.distance(a)<33 and ball.ycor() in [300,250,200,150]:
                a.clear()
                a.hideturtle()
                scores.update()
                brick_list.remove(a)
        
        if not brick_list:
            wall_maker()
        
        screen.update() 
    
Game_logic()   

screen.mainloop()