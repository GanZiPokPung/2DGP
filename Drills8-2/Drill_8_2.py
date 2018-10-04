from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

running = True
frame = 0

posX, posY = 600, 500
checkRight = 0

size = 9
points = [(random.randint(400, 800), random.randint(300, 700)) for i in range(size)]
points.insert(0,(posX, posY))
size = size + 1
n = 3

def move_curve(p1, p2, p3, p4):
    global frame
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        if(p2[0] < p3[0]):
            checkRight = 1
        else :
            checkRight = 0

        character.clip_draw(frame * 100, checkRight * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)
        get_events()

open_canvas(KPU_WIDTH, KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

while running:
    move_curve(points[n-3],points[n-2],points[n-1], points[n])
    n = (n + 1) % size

close_canvas()




