from turtle import Turtle

class bricks(Turtle):
    def __init__(self,value_x,value_y):
        super().__init__()
        self.penup()
        self.goto(value_x,value_y)
        self.shape("square")
        self.speed(0)
        
    def move(self):
        self.forward(50)
    
    def left(self):
        self.backward(50)
       
        