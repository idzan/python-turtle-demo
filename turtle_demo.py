import turtle

john = turtle.Turtle()
john.getscreen().bgcolor("#3d3d3d")
john.penup()
john.goto((-200,100))
john.pendown()

def stars(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            stars(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()

stars(john, 360)
turtle.done()