from turtle import Turtle

class balling(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.8,0.8)
        self.penup()
        self.new_x=10
        self.new_y=10
    
    def move(self):
        x=self.xcor()+self.new_x
        y=self.ycor()+self.new_y
        self.goto(x,y)
        
        
    def wallbounce(self):
        self.new_x *=-1
        
    def wallupper(self):
        self.new_y *=-1
        
    def bounce(self):
        self.new_y *=-1