import turtle

shmaggy = turtle.Turtle()
shmaggy.getscreen().bgcolor("#3d3d3d")
shmaggy.penup()
shmaggy.goto((-100,75))
shmaggy.pendown()

def stars(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(20):
            turtle.forward(size)
            stars(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()

stars(shmaggy, 360)
turtle.done()