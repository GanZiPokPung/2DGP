import game_framework
from pico2d import *
import main_state

name = "PauseState"
image = None
blinkcheck = True
time = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_o):
                resume()


def draw():
    clear_canvas()
    game_framework.stack[-2].pause()

    if blinkcheck == True:
        image.draw(400, 300)

    update_canvas()

   

def update():
    global time
    global blinkcheck
    if time > 1.0:
        if blinkcheck == False:
            blinkcheck = True
        else:
            blinkcheck = False
        time = 0
    time += 0.01


def pause():
    pass


def resume():
    game_framework.pop_state()


