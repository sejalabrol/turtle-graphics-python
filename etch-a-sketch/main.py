from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
tim = Turtle(shape="triangle")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    screen.reset()
    """
    # or 
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    """


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
