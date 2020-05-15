class Drawer:
    def __init__(self, turtle_screen, raw_turtle):
        self.screen = turtle_screen
        self.turtle = raw_turtle
        self.turtle.hideturtle()
        self.turtle.pensize(2)

    def basement(self):
        self.turtle.penup()
        self.turtle.goto(40, -60)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.forward(125)
            self.turtle.right(90)
            self.turtle.forward(25)
            self.turtle.right(90)
        self.turtle.end_fill()
        self.turtle.forward(62.5)

    def main_bar(self):
        self.turtle.left(90)
        self.turtle.forward(150)

    def upper_bar(self):
        self.turtle.left(90)
        self.turtle.forward(100)

    def rope(self):
        self.turtle.left(90)
        self.turtle.forward(15)

    def head(self):
        self.turtle.right(90)
        self.turtle.circle(15)

    def body(self):
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(30)
        self.turtle.pendown()
        self.turtle.forward(45)

    def left_foot(self):
        self.turtle.right(45)
        self.turtle.forward(35)
        self.turtle.penup()
        self.turtle.back(35)

    def right_foot(self):
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.forward(35)
        self.turtle.penup()
        self.turtle.back(35)

    def left_arm(self):
        self.turtle.left(135)
        self.turtle.forward(20)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.forward(25)

    def right_arm(self):
        self.turtle.back(50)
