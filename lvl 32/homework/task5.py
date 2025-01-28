from turtle import*
def draw_square(x_cor,y_cor):
    penup()
    goto(x_cor,y_cor)
    pendown()

for i in range (4):
    forward(200)
    left(90)
    print(i)

right(90)
draw_square(200,200)
for i in range (4):
    forward(200)
    left(90)
    print(i)
draw_square(-400,200)
for i in range (4):
    forward(200)
    left(90)
    print(i)
draw_square(-200,200)
for i in range (4):
    forward(200)
    left(90)
    print(i)
draw_square(-400,-400)
for i in range (4):
    forward(200)
    left(90)
    print(i)
draw_square(-200,200)
for i in range (4):
    forward(200)
    left(90)
    print(i)
exitonclick()