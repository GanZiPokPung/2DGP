from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


position = {132 : 243, 535 : 470,
            477 : 203, 715 : 136, 316 : 225,
            510 : 92, 692 : 518, 682 : 336, 712 : 349,
            203 : 535}


def run_from_pos_to_pos():
    frame = 0
    x, y = 203, 535

    for posX, posY in position.items():
        count = 0
        gotoX = (posX - x) / 100
        gotoY = (posY - y) / 100

        if(posX - x) > 0:
            checkRight = True
        else:
            checkRight = False

        while count <= 100 :
            clear_canvas()
            grass.draw(400, 30)
            if checkRight == True:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
            else:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            count += 1
            x += gotoX
            y += gotoY
            frame = (frame + 1) % 8
            delay(0.05)


while True:
    run_from_pos_to_pos()


close_canvas()

