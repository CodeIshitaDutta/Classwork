"""
this code will create a windmill scene with flowers and
grass that looks like an old, traditional setting with 
clouds in the background.
first, we will create the blue background.
then, we add on the base building structure.
next, we will add the grass and flowers.
then, we go onto the windmill blades and add their design.
lastly, we create the clouds for the background.
"""
#create the turtle
import turtle as trtl
drawer =trtl.Turtle()
drawer.speed(0)

#background
drawer.fillcolor("sky blue")
drawer.penup()
drawer.goto(-300,-350)
drawer.pendown()
drawer.begin_fill()
for i in range(2):
    drawer.forward(600)
    drawer.left(90)
    drawer.forward(700)
    drawer.left(90)
drawer.end_fill()

#base building
drawer.penup()
drawer.goto(-90,-350)
drawer.pencolor("brown")
drawer.fillcolor("brown")
drawer.pendown()
drawer.begin_fill()
drawer.forward(180)
drawer.setheading(95)
drawer.forward(450)
drawer.setheading(180)
drawer.forward(100)
drawer.setheading(265)
drawer.forward(450)
drawer.setheading(0)
drawer.end_fill()

# make a door for the building
drawer.penup()
drawer.pencolor("black")
drawer.fillcolor("beige")
drawer.begin_fill()
drawer.goto(-40,-350)
for i in range (2):
  drawer.forward(80)
  drawer.left(90)
  drawer.forward(190)
  drawer.left(90)
drawer.end_fill()
drawer.penup()
drawer.goto(0,-350)
drawer.setheading(90)
drawer.pendown()
drawer.forward(190)

#the grass
def grass_blades(color, rotation):
    drawer.pencolor(color)
    drawer.fillcolor(color)
    drawer.begin_fill()
    blade_length = 10 + rotation % 5
    drawer.setheading(90 + blade_length)
    drawer.forward(blade_length * 2)
    drawer.setheading(270 - blade_length)
    drawer.forward(blade_length*2)
    drawer.setheading(0)
    drawer.forward(20)
    drawer.end_fill()
grass_start_point = [-290, -293, -287]
count = 0
grass_colors = ["light green", "green", "dark green"]
for i in range (3):
    drawer.penup()
    drawer.goto(grass_start_point[i],-350)
    drawer.pendown()
    for j in range(60):
        count = count + j
        grass_blades(grass_colors[i], count)
        count = 0

#the flowers
def flowers(color):
    drawer.pencolor(color)
    drawer.setheading(0)
    drawer.forward(5)
    drawer.pendown()
    drawer.circle(5)
    drawer.penup()
    drawer.forward(10)
    drawer.setheading(90)
    drawer.forward(5)
    direction = 0
    drawer.setheading(180)
    drawer.forward(10)
    for i in range(6):
        drawer.setheading(direction)
        drawer.forward(10)
        drawer.pendown()
        drawer.circle(5)
        drawer.penup()
        drawer.backward(10)
        direction = direction + 60
count = 0
drawer.penup()
drawer.goto(-292,-320)
flower_color = ["coral", "lavender", "navy blue"]
drawer.pensize(4)
while count < 20:
        flowers(flower_color[count % 3])
        drawer.setheading(85)
        drawer.backward(5)
        drawer.setheading(0)
        drawer.forward(25.5)
        count = count + 1

#clouds
drawer.penup()
drawer.goto(-420,250)
drawer.pensize(10)
drawer.pencolor("white")
for i in range(16):
  if i % 10 != 0:
    drawer.setheading(75)
    drawer.pendown()
    drawer.forward(20)
    drawer.backward(20)
    drawer.penup()
    drawer.setheading(0)
    drawer.forward(30)
  else:
    drawer.setheading(0)
    drawer.penup()
    drawer.forward(150)

#blades
drawer.penup()
drawer.goto(-20,100)
drawer.pencolor("brown")
drawer.fillcolor("beige")
drawer.pensize(4)
drawer.pendown()
drawer.begin_fill()
direction = 95
turn = 45
for i in range (4):
  drawer.setheading(direction)
  for i in range(45):
    drawer.forward(5)
    drawer.right(1)
  drawer.setheading(direction + 260)
  drawer.pensize(25)
  drawer.forward(120)
  drawer.pensize(4)
  drawer.right(direction + turn)
  for i in range(42):
    drawer.forward(5)
    drawer.left(1)
  drawer.right(4)
  drawer.forward(40)
  direction = direction - 90
  turn = turn + 90
drawer.end_fill()

#blade designs
go_x_cor = [-5, 45, 10, -40]
go_y_cor = [110,75, 25, 60]
direction = [95, 5, 275, 185]
for i in range(4):
    drawer.penup()
    drawer.goto(go_x_cor[i],go_y_cor[i])
    drawer.setheading(direction[i])
    for j in range(10):
        drawer.pendown()
        drawer.circle(4)
        drawer.right(4)
        drawer.penup()
        drawer.forward(20)

#keeps the screen from disappearing
wn = trtl.Screen()
wn.mainloop()
