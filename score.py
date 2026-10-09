from turtle import Turtle

class scoring(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("gray")
        self.value=0
        self.show()
        
    def show(self):
        self.clear()
        self.write(self.value,font=("Arial",20,"bold"))
        
    def update(self):
        self.value+=1
        self.show()
    
    def reset(self):
        self.value=0
        self.show()