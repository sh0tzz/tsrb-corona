import turtle
import time
import random
import sys
from playsound import playsound
import _thread

def goUp():
    player.dy = 0
    dy = player.dy
    dy += 7
    if dy > 20:
        dy = 20
    player.dy = dy

def resetPipe(pipe_top, pipe_bot):
    rand_num = random.randint(-175,175)
    pipe_top.goto(300, 325+rand_num)
    pipe_bot.goto(300, -325+rand_num)

def QUIT():
    sys.exit(1)

#variables
#other
GRAV = -0.35


#screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = "blue"

#player
PLAYER_COLOR = "yellow"
PLAYER_SHAPE = "circle"
PLAYER_POS = (-150, 0)

#pipes
PIPE_COLOR = "green"
PIPE_SHAPE = "square"




wn = turtle.Screen()
wn.title("TSRB WANTS COVID")
wn.bgcolor(BACKGROUND_COLOR)
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.bgpic("background.gif")
wn.tracer(0)
wn.cv._rootwindow.resizable(False, False)
wn.register_shape("bird.gif")
wn.register_shape("pipeUp.gif")
wn.register_shape("pipeDown.gif")

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color(PLAYER_COLOR)
player.shape("bird.gif")
#player.shapesize(1.7, 1.7)
player.goto(PLAYER_POS)
player.dy = 1

#----------------------------

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(-10, 100)

#----------------------------

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color(PIPE_COLOR)
pipe1_top.shape("pipeUp.gif")
pipe1_top.dx = -3
pipe1_top_value = 1

pipe1_bot = turtle.Turtle()
pipe1_bot.speed(0)
pipe1_bot.penup()
pipe1_bot.color(PIPE_COLOR)
pipe1_bot.shape("pipeDown.gif")
pipe1_bot.dx = -3

#--------------------------

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color(PIPE_COLOR)
pipe2_top.shape("pipeUp.gif")
pipe2_top.dx = -3
pipe2_top_value = 1

pipe2_bot = turtle.Turtle()
pipe2_bot.speed(0)
pipe2_bot.penup()
pipe2_bot.color(PIPE_COLOR)
pipe2_bot.shape("pipeDown.gif")
pipe2_bot.dx = -3

#---------------------------

pipe3_top = turtle.Turtle()
pipe3_top.speed(0)
pipe3_top.penup()
pipe3_top.color(PIPE_COLOR)
pipe3_top.shape("pipeUp.gif")
pipe3_top.dx = -3
pipe3_top_value = 1

pipe3_bot = turtle.Turtle()
pipe3_bot.speed(0)
pipe3_bot.penup()
pipe3_bot.color(PIPE_COLOR)
pipe3_bot.shape("pipeDown.gif")
pipe3_bot.dx = -3

#---------------------------

#keyboard bind
wn.listen()
wn.onkeyrelease(goUp, "space")
wn.onkeyrelease(QUIT, "q")

#variables
score = 0
dead_flag = 0
gravity = 0

#set pipes
rand_num = random.randint(-175, 175)
pipe1_top.goto(100, 325+rand_num)
pipe1_bot.goto(100, -325+rand_num)
rand_num = random.randint(-175, 175)
pipe2_top.goto(350, 325+rand_num)
pipe2_bot.goto(350, -325+rand_num)
rand_num = random.randint(-175, 175)
pipe3_top.goto(600, 325+rand_num)
pipe3_bot.goto(600, -325+rand_num)

wn.update()

time.sleep(1.5)

_thread.start_new_thread(playsound, ('comfy_music.mp3',))

#main game loop
while True:
    try:
        #screen update
        wn.update()
        time.sleep(0.02)
        
        #gravity
        dy = player.dy
        dy += GRAV
        if dy < -10:
            dy = -10
        player.dy = dy

        
        #move player
        y = player.ycor()
        y += player.dy
        player.sety(y)

        #move pipes
        x = pipe1_top.xcor()
        x += pipe1_top.dx
        pipe1_top.setx(x)
        pipe1_bot.setx(x)

        x = pipe2_top.xcor()
        x += pipe2_top.dx
        pipe2_top.setx(x)
        pipe2_bot.setx(x)

        x = pipe3_top.xcor()
        x += pipe3_top.dx
        pipe3_top.setx(x)
        pipe3_bot.setx(x)

        #check for collisions
        if (player.xcor() + 32 > pipe1_top.xcor() - 20) and (player.xcor() - 32 < pipe1_top.xcor() + 20):
            if (player.ycor() + 45 > pipe1_top.ycor() - 220) or (player.ycor() - 45 < pipe1_bot.ycor() + 220):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 25, "normal"))
                wn.update()
                dead_flag = True
        if (player.xcor() + 32 > pipe2_top.xcor() - 20) and (player.xcor() - 32 < pipe2_top.xcor() + 20):
            if (player.ycor() + 45 > pipe2_top.ycor() - 220) or (player.ycor() - 45 < pipe2_bot.ycor() + 220):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 25, "normal"))
                wn.update()
                dead_flag = True
        if (player.xcor() + 32 > pipe3_top.xcor() - 20) and (player.xcor() - 32 < pipe3_top.xcor() + 20):
            if (player.ycor() + 45 > pipe3_top.ycor() - 220) or (player.ycor() - 45 < pipe3_bot.ycor() + 220):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 25, "normal"))
                wn.update()
                dead_flag = True

        #check for score
        if pipe1_top.xcor() + 30 < player.xcor() - 10:
            score += pipe1_top_value
            pipe1_top_value = 0
            pen.clear()
            pen.write(f'covid cases {score}', move=False, align="center", font=("Arial", 32, "normal"))

        if pipe2_top.xcor() + 30 < player.xcor() - 10:
            score += pipe2_top_value
            pipe2_top_value = 0
            pen.clear()
            pen.write(f'covid cases {score}', move=False, align="center", font=("Arial", 32, "normal"))
            
        if pipe3_top.xcor() + 30 < player.xcor() - 10:
            score += pipe3_top_value
            pipe3_top_value = 0
            pen.clear()
            pen.write(f'covid cases {score}', move=False, align="center", font=("Arial", 32, "normal"))

                
        #reset pipes
        x = pipe1_top.xcor()
        if x < -450:
            resetPipe(pipe1_top, pipe1_bot)
            pipe1_top_value = 1
        
        x = pipe2_top.xcor()
        if x < -450:
            resetPipe(pipe2_top, pipe2_bot)
            pipe2_top_value = 1

        x = pipe3_top.xcor()
        if x < -450:
            resetPipe(pipe3_top, pipe3_bot)
            pipe3_top_value = 1

        #check if game over
        if dead_flag == True:
            time.sleep(1.5)
            #reset pen
            pen.clear()
            #reset pipes
            rand_num = random.randint(-175, 175)
            pipe1_top.goto(100, 325+rand_num)
            pipe1_bot.goto(100, -325+rand_num)
            rand_num = random.randint(-175, 175)
            pipe2_top.goto(350, 325+rand_num)
            pipe2_bot.goto(350, -325+rand_num)
            rand_num = random.randint(-175, 175)
            pipe3_top.goto(600, 325+rand_num)
            pipe3_bot.goto(600, -325+rand_num)
            #reset player
            player.goto(PLAYER_POS)
            #reset score
            score = 0
            pen.write(f'covid cases {score}', move=False, align="center", font=("Arial", 32, "normal"))
            #reset dead_flag
            dead_flag = 0
            #reset y
            dy = 0
            player.dy = 0
            gravity = 0
            time.sleep(1.5)
    except:
        sys.exit(1)