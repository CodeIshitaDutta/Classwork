#import statements
import turtle as trtl
import random as rand

apple_image = ".\\a123\\images\\save_apple.GIF" #this sets up all the different turtles
wn = trtl.Screen()
wn.addshape(apple_image)
wn.setup(width=1.0, height=1.0)
wn.bgpic(".\\a123\\images\\background.GIF")
apple = trtl.Turtle()

#the writing turtle at the top
writer = trtl.Turtle()
writer.penup()
writer.goto(0,200)
writer.pendown()

#the typing turtle at the bottom
drawer = trtl.Turtle()
drawer.penup()
drawer.goto(300,-200)
drawer.pendown()

#this is a list of letters that we will type for the apple
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l"]

#this creates the apple turtle
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

#this is the apple falling from the tree.
def apple_falls():
  apple.setheading(270)
  apple.penup()
  apple.forward(200)

#this is to get a new apple at the top of the tree
def new_apple():
  apple.hideturtle()
  new_x_cor = rand.randint(-100,100)
  new_y_cor = rand.randint(0,75)
  apple.goto(new_x_cor, new_y_cor)
  apple.showturtle()

#this function gives the different letters to type
def write_letter():
  writer.clear()
  writer.pendown()
  writer.color("blue")
  writer.write(letter_from_list, font=("Arial", 20, "bold"))

# This function takes care of font and color for the typing part.
def draw_letter():
  drawer.clear()
  drawer.color("lavender")
  drawer.write(letter_from_list, font=("Arial", 20, "bold")) 
  apple_falls()
  new_apple()

draw_apple(apple)

letter_from_list = letter_list[rand.randint(0,len(letter_list) - 1)]
write_letter()
wn.onkeypress(draw_letter, str(letter_from_list))

wn.listen()


trtl.mainloop()
