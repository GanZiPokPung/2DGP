from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

rightCheck = True

x = 0
frame = 0

while True:
    clear_canvas()
    grass.draw(400, 30)

    if rightCheck == True :
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        x += 5
        if x > 800:
            rightCheck = False
    else :
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        x -= 5
        if x < 0:
            rightCheck = True

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()


close_canvas()
