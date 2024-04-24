# a121_catch_a_turtle.py
"""these are all the import programs and turtles"""
import turtle as trtl
import random as rand

#tammy the turtle
tammy =trtl.Turtle()
tammy.shape("turtle")
tammy.shapesize(2)
tammy.fillcolor("light pink")

#the scoring mechanism
scorer =trtl.Turtle()
scorer.penup()
scorer.goto(-200,-200)
scorer.hideturtle()
score = 0
font_setup = ("Comic Sans MS", 20, "normal")

#the timer mechanism
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter =  trtl.Turtle()
counter.penup()
counter.goto(200,-200)
counter.hideturtle()

"""these are the functions that make the game work"""

#Tying the functions together to show what happens on clicking tammy
def tammy_is_clicked(x, y):
    change_position()
    update_tammy_score()
    time_keeper()

#how to change tammy the turtle's location
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    tammy.penup()
    tammy.hideturtle()
    tammy.goto(new_xpos,new_ypos)
    tammy.pendown()
    tammy.showturtle()

#this adds to the score when tammy the turtle is clicked
def update_tammy_score():
  global score 
  score += 1
  scorer.pendown()
  scorer.clear()
  scorer.write("score: " + str(score), font = font_setup)

#counting down the time as a timer
def time_keeper():
  global timer, timer_up
  counter.pendown()
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    tammy.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(time_keeper, counter_interval) 

tammy.onclick(tammy_is_clicked)

wn = trtl.Screen()
wn.ontimer(time_keeper, counter_interval) 
wn.mainloop()
