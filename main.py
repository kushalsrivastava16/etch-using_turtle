from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def to_right():
    x = tim.heading()
    tim.setheading(x + 10)


def to_left():
    x = tim.heading()
    tim.setheading(x - 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.reset()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=to_right)
screen.onkey(key="a", fun=to_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
