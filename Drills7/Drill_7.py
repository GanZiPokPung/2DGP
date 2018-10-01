from pico2d import *
import random



KPU_WIDTH, KPU_HEIGHT = 1280, 1024

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

posX, posY = 400, 300
gotoX, gotoY = 0, 0
checkRight = 0
count = 101

size = 10
points = [(random.randint(400, 1000), random.randint(300, 1000)) for i in range(size)]
n = 1

def move_to_point_character(p1, p2):
    global frame
    for i in range(0, 100 + 1, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        goX = (1 - t) * p1[0] + t * p2[0]
        goY = (1 - t) * p1[1] + t * p2[1]
        if (p2[0] - p1[0]) < 0 :
                checkRight = 0
        else:
                checkRight = 1
        character.clip_draw(frame * 100, checkRight * 100, 100, 100, goX, goY)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

while running:
    move_to_point_character(points[n-1], points[n])
    n = (n + 1) % size

close_canvas()




