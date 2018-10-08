from pico2d import *
import random

# Game object class here
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

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

# boy1 = Boy()
# boy2 = Boy()
# boy3 = Boy()
# boy4 = Boy()
# boy5 = Boy()
# boy6 = Boy()
# boy7 = Boy()
# boy8 = Boy()
# boy9 = Boy()
# boy10 = Boy()
# boy11 = Boy()

#team = [boy1, boy2, boy3, boy4, boy5, boy6, boy7, boy8, boy9, boy10, boy11]
#위 코드를 한번에 해줌
#틀린코드
#team = [Boy()] * 11
#맞는코드
team = [Boy() for i in range(11)]

grass = Grass()

running = True;
# game main loop code

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

# finalization code
close_canvas()