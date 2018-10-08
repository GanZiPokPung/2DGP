from pico2d import *
import random

# Obj Class
class Grass:
    #생성자 : 파이썬은 멤버변수를 만듬과 동시에 초기화가 가능
    def __init__(self):
        self.image = load_image('grass.png')
    #행위 : 함수로 만든다.
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#init
open_canvas()
team = [Boy() for i in range(11)]
grass = Grass()
running = True;

#main
while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    update_canvas()

    delay(0.05)

#close
close_canvas()