import turtle

# Setup screen
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

# 1. Main eye base (Red background circle)
draw_circle("#bf0404", 180, 0, -180)

# 2. Black outer ring
t.penup()
t.goto(0, -180)
t.pendown()
t.pencolor("black")
t.width(8)
t.circle(180)



# 3. Central black pupil
draw_circle("black", 35, 0, -35)


# 4. Draw Itachi's 3 Mangekyo Blades
def draw_blade(angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    
    # Outer curve of the blade
    t.circle(100, 120)
    
    
    
    # Sharp tip point and inner curve back to center
    t.left(140)
    t.circle(-135, 50)
    
    # Return to center pupil
   
    t.end_fill()

# Render the 3 pinwheel blades evenly spaced at 120-degree intervals
for i in range(3):
    draw_blade(i * 120)
turtle.mainloop()
