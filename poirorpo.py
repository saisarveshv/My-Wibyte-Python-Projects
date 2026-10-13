import turtle
poi=turtle.Screen()
poi.screensize(10000,10000)
it=turtle.Turtle()
it.showturtle()
it.penup()
it.right(45)
it.goto(-300,-300)
it.fillcolor('#FDE0D9')
it.begin_fill()

it.pendown()

it.circle(2500,90)
it.circle(3500,90)
it.circle(2500,90)
it.circle(3500,90)
it.end_fill()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()



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
def draw_itachi_hair():
    # Start at the top left of the head
    it.penup()
    it.goto(-150, 200) 
    it.pendown()
    
    # Hair color fill
    it.begin_fill()
    it.fillcolor("#1c1c22") # Dark grey/black for Itachi's hair

    # --- TOP OUTER HAIR & SPIKES ---
    # Using your large arc scaling to build the outer volume
    it.setheading(60)
    it.circle(-2500, 30) # Outward curve
    it.circle(-3500, 25) # Top curve
    
    # First sharp back spike
    it.setheading(240)
    it.forward(120)
    it.setheading(30)
    it.circle(-2500, 20)
    
    # --- RIGHT SIDE FRAMING BANGS ---
    # The long bang framing the right side of his face
    it.setheading(-80)
    it.circle(-3500, 35)
    
    # Sharp tip of the right bang
    it.setheading(110)
    it.circle(2500, 15)
    
    # --- CENTER M-SHAPED FOREHEAD BANGS ---
    # These sit right above his forehead protector
    it.setheading(160)
    it.forward(80)   # Right peak of the 'M'
    it.setheading(-60)
    it.forward(90)   # Center point dropping down between eyes
    it.setheading(120)
    it.forward(90)   # Left peak of the 'M'
    
    # --- LEFT SIDE FRAMING BANGS ---
    # Long bang framing the left side of his face
    it.setheading(-110)
    it.circle(3500, 30)
    
    # Sharp tip of the left bang returning upward
    it.setheading(70)
    it.circle(-2500, 25)
    
    # Close the hair shape back to the start
    it.goto(-150, 200)
    it.end_fill()
    
    # --- PONYTAIL (Back of the neck) ---
    it.penup()
    it.goto(80, -100) # Positioning near the lower right neck
    it.pendown()
    it.begin_fill()
    it.setheading(-90)
    it.circle(-800, 40) # Curve of the loose ponytail
    it.setheading(70)
    it.circle(800, 45)
    it.end_fill()

# Run the drawing
draw_itachi_hair()


turtle.mainloop()
