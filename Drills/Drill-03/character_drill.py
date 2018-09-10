from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

angle = 180
totalMove = 0

SquareCheck = True
CircleCheck = False

def SquareMove() :
    global x
    global y
    global totalMove
    global SquareCheck
    global CircleCheck

    speed = 10
    
    if(y == 90 and x < 800):
        x = x + speed
        totalMove = totalMove + speed
    elif(x == 800 and y < 600):
        y = y + speed
        totalMove = totalMove + speed
    elif(y == 600 and x > 0):
        x = x - speed
        totalMove = totalMove + speed
    elif(x == 0 and y > 90):
        y = y - speed
        totalMove = totalMove + speed

    if(totalMove > 2620):
        SquareCheck = False
        CircleCheck = True
        totalMove = 0
        return 0

    character.draw_now(x, y)

        
def CircleMove() :
    global x
    global y
    global angle
    global SquareCheck
    global CircleCheck
    
    x = 400
    y = 330
    angle = angle + 2

    x = x + (math.sin(math.radians(angle)) * 240)
    y = y + (math.cos(math.radians(angle)) * 240)

    if(angle >= 540):
        SquareCheck = True
        CircleCheck = False
        angle = 180
        x = 400
        y = 90
        return 0

    character.draw_now(x, y)

while(True):
    clear_canvas_now()
    
    if (SquareCheck == True):
        SquareMove()
    elif (CircleCheck == True):
        CircleMove()
        
    grass.draw_now(400, 30)
    delay(0.01)
    
close_canvas()
