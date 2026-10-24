import turtle
s=turtle.Turtle()

ts=s.getscreen()
i=turtle.Screen()
i.title("Itachi Mangekyo Sharingan")
i.screensize(600,600)
def draw_line(x0,y0,x1,y1):
    s.penup()
    s.goto(x0,y0)
    s.pendown()
    s.goto(x1,y1)
def draw_rectangle(x0,y0,h,l,c):
    s.fillcolor(c)
    
    s.begin_fill()
    draw_line(x0,y0,x0+l,y0)
    draw_line(x0+l,y0,x0+l,y0+h)
    draw_line(x0+l,y0+h,x0,y0+h)
    draw_line(x0,y0+h,x0,y0)
    s.end_fill()
    

ts.tracer(0)
n_cols=21
x_val=-200
y_val=200

for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<8:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>7 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=-200
y_val=60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>15 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=0
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=-200
y_val=-40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=-200
y_val=-80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>11 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
            draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=-200
y_val=-200
for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


ts.tracer(0)
n_cols=21
x_val=200
y_val=200

for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=200
y_val=180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<8:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>7 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=200
y_val=140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=200
y_val=120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=200
y_val=100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<9:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>8 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<3:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>2 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20

n_cols=21
x_val=200
y_val=60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>15 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=0
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-20
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>11 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=200
y_val=-40
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>4 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-60
for jj in range(n_cols):
    if jj<1:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>0 and jj<2:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>1 and jj<6:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>5 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20



n_cols=21
x_val=200
y_val=-80
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<4:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>3 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<15:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>14 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    
    elif jj>18 and jj<20:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-100
for jj in range(n_cols):
    if jj<2:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>1 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>13 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>17 and jj<19:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-120
for jj in range(n_cols):
    if jj<3:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>2 and jj<12:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>11 and jj<17:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>16 and jj<18:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-140
for jj in range(n_cols):
    if jj<4:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>3 and jj<5:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>6 and jj<10:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>9 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>15 and jj<17:
            draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-160
for jj in range(n_cols):
    if jj<5:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>4 and jj<7:
        draw_rectangle(x_val,y_val,20,20,"black")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"red")
    elif jj>13 and jj<16:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-180
for jj in range(n_cols):
    if jj<7:
        draw_rectangle(x_val,y_val,20,20,"white")
    elif jj>6 and jj<14:
        draw_rectangle(x_val,y_val,20,20,"black")
    else:
         draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20


n_cols=21
x_val=200
y_val=-200
for jj in range(n_cols):
    draw_rectangle(x_val,y_val,20,20,"white")
    x_val=x_val+20
ts.update()
turtle.mainloop()

