from pico2d import *
from math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x = 0
frame = 0

position = {132 : 243, 535 : 470,
            477 : 203, 715 : 136, 316 : 225,
            510 : 92, 692 : 518, 682 : 336, 712 : 349,
            203 : 535}


def run_from_pos_to_pos():
    x, y = 203, 535

    for posX, posY in position.items():
        checkX = 0
        distX = math.fabs(posX - x)
        distY = math.fabs(posY - y)
        inclination = distY / distX

        if(posX - x) > 0:
            checkRight = True
        else:
            checkRight = False

        while checkX < distX :
            clear_canvas()
            grass.draw(400, 30)
            if checkRight == True:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
                x += 1
                y = y + (inclination * x)
            else:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
                x -= 1
                y = y + (inclination * x)
            checkX += 1
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)


while True:
    run_from_pos_to_pos()


close_canvas()

