import turtle
s=turtle.Screen()
i=turtle.Turtle()

s.setup(1500,1000)
s.bgcolor("#03002E")
i.speed(2)
i.penup()
i.pencolor("#FDE0D9")
i.fillcolor('#FDE0D9')

def draw_circle(color, radius, x, y):
    i.penup()
    i.fillcolor(color)
    i.goto(x, y)
    i.pendown()
    i.begin_fill()
    i.circle(radius)
    i.end_fill()


i.showturtle()

turtle.mainloop()