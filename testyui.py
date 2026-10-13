import turtle


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Itachi Mangekyo Sharingan")
screen.bgcolor('Black')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


draw_circle("#bf0404", 180, 0, -180)


t.penup()
t.goto(0, -180)
t.pendown()
t.pencolor("black")
t.width(8)
t.circle(180)




draw_circle("black", 35, 0, -35)



def draw_blade(angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    
    
    t.circle(100, 120)
    
    
    
    
    t.left(140)
    t.circle(-135, 50)
    
    
   
    t.end_fill()


for i in range(3):
    draw_blade(i * 120)
turtle.mainloop()
